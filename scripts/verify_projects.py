#!/usr/bin/env python3
"""Validate projects.json and keep generated manifests honest."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    data = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))
    projects = data.get("projects", [])
    errors: list[str] = []
    seen: dict[str, str] = {}
    for project in projects:
        path = project.get("path", "")
        if not path or path.startswith("/") or ".." in Path(path).parts:
            errors.append(f"bad path: {project!r}")
            continue
        if path in seen:
            errors.append(f"duplicate path {path}: {seen[path]} and {project.get('repo')}")
        seen[path] = project.get("repo", "?")
        if project.get("host") not in ("codeberg", "gitlab", "github"):
            errors.append(f"bad host: {project!r}")
        if not str(project.get("url", "")).endswith(".git"):
            errors.append(f"bad url: {project!r}")

    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_manifest.py"), "--check"],
        cwd=ROOT,
    )
    if result.returncode:
        errors.append("generated manifests are stale; run scripts/build_manifest.py")

    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors), file=sys.stderr)
        return 1
    print(f"OK: {len(projects)} projects, {len(seen)} unique paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
