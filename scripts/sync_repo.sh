#!/usr/bin/env bash
# Optional full-tree workflow using Google's `repo` tool.
# The GitHub meta-repo is the manifest; Codeberg remains the source host.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANIFEST_URL="${ONYX_MANIFEST_URL:-$(git -C "$ROOT" remote get-url origin 2>/dev/null || true)}"
BRANCH="${ONYX_MANIFEST_BRANCH:-main}"
GROUPS="${ONYX_GROUPS:-}"
JOBS="${ONYX_JOBS:-4}"
WORK="${ONYX_WORKTREE:-$ROOT/worktree}"

if [[ -z "$MANIFEST_URL" ]]; then
  echo "Set ONYX_MANIFEST_URL to the GitHub/Git remote of OnyxProject" >&2
  exit 2
fi
if ! command -v repo >/dev/null 2>&1; then
  echo "repo is not installed: https://source.android.com/docs/setup/download" >&2
  exit 2
fi

mkdir -p "$WORK"
cd "$WORK"
repo init -u "$MANIFEST_URL" -b "$BRANCH" --no-clone-bundle
if [[ -n "$GROUPS" ]]; then
  repo sync -c -j"$JOBS" --no-tags -g "$GROUPS"
else
  repo sync -c -j"$JOBS" --no-tags
fi
