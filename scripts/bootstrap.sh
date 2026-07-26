#!/usr/bin/env bash
set -euo pipefail

# Clone all Veliform product repos into ~/WORKSPACE/veliform/
# Usage: ./scripts/bootstrap.sh [target_dir]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
META_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
TARGET="${1:-${HOME}/WORKSPACE/veliform}"

mkdir -p "${TARGET}"

echo "Veliform bootstrap → ${TARGET}"
echo ""

clone_repo() {
  local git_url="$1"
  local dest="$2"
  if [[ -d "${dest}/.git" ]]; then
    echo "  ✓ exists  ${dest}"
    return 0
  fi
  if [[ -d "${dest}" ]]; then
    echo "  ! skip (directory exists, not git): ${dest}" >&2
    return 0
  fi
  echo "  → clone   ${git_url} → ${dest}"
  git clone "${git_url}" "${dest}"
}

# meta (this repo)
if [[ "${META_DIR}" == "${TARGET}/meta" ]] || [[ -d "${TARGET}/meta/.git" ]]; then
  echo "  ✓ meta    ${TARGET}/meta"
else
  clone_repo "https://github.com/josefwebdeveloper/veliform-meta.git" "${TARGET}/meta"
fi

# voice
clone_repo "https://github.com/josefwebdeveloper/voice-agent.git" "${TARGET}/voice"

echo ""
echo "Done. Next steps:"
echo "  1. Open ${TARGET}/meta/veliform.code-workspace in Cursor"
echo "  2. Copy .env → ${TARGET}/voice/apps/voice-server/.env"
echo "  3. Notion CEO DBs — ${TARGET}/meta/docs/NOTION_CEO.md"
echo "  4. gh auth login && railway login (optional)"
