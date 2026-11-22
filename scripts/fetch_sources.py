#!/usr/bin/env python3
"""Clone/update the Onyx Project source inventory without hard-coded tokens.

Examples:
  python3 scripts/fetch_sources.py --list
  python3 scripts/fetch_sources.py --host codeberg --group system --depth 1
  python3 scripts/fetch_sources.py --host all --dest sources --jobs 4
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import shutil
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PROJECTS = ROOT / "projects.json"
PRINT_LOCK = threading.Lock()


def log(message: str) -> None:
    with PRINT_LOCK:
        print(message, flush=True)


def load_projects() -> list[dict]:
    data = json.loads(PROJECTS.read_text(encoding="utf-8"))
    return data["projects"]


def matches(project: dict, args: argparse.Namespace) -> bool:
    if args.host != "all" and project["host"] != args.host:
        return False
    if args.group and project["group"] not in args.group.split(","):
        return False
    if args.only and not any(
            fnmatch.fnmatch(project["repo"], pattern)
            or fnmatch.fnmatch(project["path"], pattern)
            for pattern in args.only):
        return False
    if args.exclude and any(
            fnmatch.fnmatch(project["repo"], pattern)
            or fnmatch.fnmatch(project["path"], pattern)
            for pattern in args.exclude):
        return False
    return True


def run_git(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
    )


def sync_one(project: dict, args: argparse.Namespace) -> tuple[str, str]:
    dest = (args.dest / project["path"]).resolve()
    if dest.exists() and not (dest / ".git").exists():
        return project["path"], f"SKIP (not a git checkout): {dest}"

    if (dest / ".git").exists():
        if not args.update:
            return project["path"], "SKIP (exists; use --update)"
        result = run_git(["fetch", "--all", "--prune"], cwd=dest)
        if result.returncode:
            return project["path"], "FAIL fetch\n" + result.stdout.strip()
        result = run_git(["pull", "--ff-only"], cwd=dest)
        if result.returncode:
            return project["path"], "FAIL pull (local changes?)\n" + result.stdout.strip()
        return project["path"], "UPDATED"

    dest.parent.mkdir(parents=True, exist_ok=True)
    command = ["clone", "--no-tags"]
    if args.depth > 0:
        command += ["--depth", str(args.depth)]
    command += [project["url"], str(dest)]
    if args.dry_run:
        return project["path"], "DRY " + " ".join(command)
    result = run_git(command)
    if result.returncode:
        return project["path"], "FAIL clone\n" + result.stdout.strip()
    return project["path"], "CLONED"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", choices=["all", "codeberg", "gitlab", "github"], default="all")
    parser.add_argument("--group", default="", help="comma separated: system,apps,tools,ecosystem,meta")
    parser.add_argument("--only", action="append", default=[], help="repo/path glob; repeatable")
    parser.add_argument("--exclude", action="append", default=[], help="repo/path glob; repeatable")
    parser.add_argument("--dest", type=Path, default=ROOT / "sources")
    parser.add_argument("--depth", type=int, default=1, help="0 = full history")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--update", action="store_true")
    parser.add_argument("--keep-going", action="store_true")
    args = parser.parse_args()

    args.dest = args.dest.expanduser().resolve()
    projects = [p for p in load_projects() if matches(p, args)]
    if not projects:
        print("no projects matched", file=sys.stderr)
        return 2

    # AOSP plus all apps is tens of GB. Never make a bare invocation download
    # everything by accident; require an explicit group or path filter.
    if not args.list and not args.dry_run and not args.group and not args.only:
        print(
            "refusing to fetch all projects: pass --group system,apps,ecosystem,tools "
            "or --only <repo/path>; use --list to inspect first",
            file=sys.stderr,
        )
        return 2

    if args.list:
        for project in projects:
            print(f"{project['host']:8} {project['group']:9} {project['path']:45} {project['url']}")
        return 0

    if shutil.which("git") is None:
        print("git not found", file=sys.stderr)
        return 2

    log(f"syncing {len(projects)} projects into {args.dest} "
        f"(depth={args.depth}, jobs={args.jobs})")
    failures: list[tuple[str, str]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        futures = {pool.submit(sync_one, project, args): project for project in projects}
        for future in as_completed(futures):
            project = futures[future]
            try:
                path, status = future.result()
            except Exception as exc:  # keep the remaining clones running
                path, status = project["path"], f"FAIL {exc!r}"
            log(f"{status:10} {path}")
            if status.startswith("FAIL"):
                failures.append((path, status))
                if not args.keep_going:
                    break

    if failures:
        print(f"\n{len(failures)} failure(s):", file=sys.stderr)
        for path, status in failures:
            print(f"  {path}: {status}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
