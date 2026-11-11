#!/usr/bin/env bash
# Bash 3.2+, offline installation. No Python, Git, Node, or administrator access.
set -euo pipefail
agent=all
scope=user
project="$PWD"
project_set=0
force=0
dry_run=0
usage() {
  cat <<'EOF'
Usage: bash install.sh [--agent all|claude-code|copilot|cursor|codex]
                       [--scope user|project] [--project PATH] [--force] [--dry-run]
Default: --agent all --scope user
Project scope defaults to the current directory; --project must already exist.
Identical installs are skipped. Different existing copies require --force,
which moves them to a backup outside the discovery directory before replacing.
EOF
}
fail() { printf 'Error: %s\n' "$*" >&2; exit 1; }
while [ "$#" -gt 0 ]; do
  case "$1" in
    --agent|--scope|--project)
      [ "$#" -ge 2 ] || fail "Missing value for $1"
      case "$1" in
        --agent) agent=$2 ;;
        --scope) scope=$2 ;;
        --project) project=$2; project_set=1 ;;
      esac
      shift 2 ;;
    --force) force=1; shift ;;
    --dry-run) dry_run=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) fail "Unknown argument: $1" ;;
  esac
done
case "$agent" in all|claude-code|copilot|cursor|codex) ;; *) fail 'Invalid agent' ;; esac
case "$scope" in user|project) ;; *) fail 'Invalid scope' ;; esac
[ "$scope" = project ] || [ "$project_set" = 0 ] || fail '--project requires --scope project'
package_root=$(CDPATH='' cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
source_dir="$package_root/afta-security"
[ -f "$source_dir/SKILL.md" ] && [ -f "$source_dir/references/catalog.json" ] || fail 'Keep install.sh beside the complete afta-security folder'
if [ "$scope" = project ]; then
  [ -d "$project" ] || fail "Project does not exist: $project"
  base=$(CDPATH='' cd -- "$project" && pwd -P)
else
  [ -n "${HOME:-}" ] && [ -d "$HOME" ] || fail 'Cannot find user home directory'
  base=$(CDPATH='' cd -- "$HOME" && pwd -P)
fi
case "$base/" in "$source_dir/"*) fail 'Choose a project outside the packaged skill source directory' ;; esac
# The shared directory covers Codex, Copilot and Cursor; Claude needs its own.
case "$agent" in
  all) roots=(.agents/skills .claude/skills) ;;
  codex) roots=(.agents/skills) ;;
  claude-code) roots=(.claude/skills) ;;
  cursor) roots=(.cursor/skills) ;;
  copilot)
    if [ "$scope" = project ]; then roots=(.github/skills); else roots=(.copilot/skills); fi ;;
esac
modes=()
# Preflight every target before making changes.
for root in "${roots[@]}"; do
  target="$base/$root/afta-security"
  [ ! -L "$target" ] || fail "Refusing a symbolic-link target: $target"
  if [ -e "$target" ]; then
    [ -d "$target" ] || fail "Destination is not a directory: $target"
    if diff -qr "$source_dir" "$target" >/dev/null 2>&1; then
      modes+=(skip)
    else
      [ "$force" = 1 ] || fail "Different install exists: $target (use --force to back it up and update)"
      modes+=(update)
    fi
  else
    modes+=(install)
  fi
done
stage=''
backup=''
active_target=''
cleanup() {
  rc=$?
  trap - EXIT
  if [ "$rc" -ne 0 ] && [ -n "$backup" ] && [ ! -e "$active_target" ]; then
    mv "$backup" "$active_target" || printf 'Restore backup manually: %s\n' "$backup" >&2
  fi
  if [ -n "$stage" ] && [ -d "$stage" ]; then rm -rf "$stage"; fi
  exit "$rc"
}
trap cleanup EXIT
i=0
for root in "${roots[@]}"; do
  target="$base/$root/afta-security"
  mode=${modes[$i]}
  i=$((i + 1))
  if [ "$mode" = skip ]; then printf 'Already installed: %s\n' "$target"; continue; fi
  if [ "$dry_run" = 1 ]; then printf 'Would %s: %s\n' "$mode" "$target"; continue; fi
  parent="$base/$root"
  mkdir -p "$parent"
  # Stage outside skill discovery directories to avoid discovering partial copies.
  stage=$(mktemp -d "$base/.afta-stage.XXXXXX")
  cp -R "$source_dir/." "$stage/"
  backup=''
  active_target="$target"
  if [ "$mode" = update ]; then
    backup_root="$base/.afta-security-backups"
    mkdir -p "$backup_root"
    backup=$(mktemp -d "$backup_root/${agent}-$(date +%Y%m%d-%H%M%S).XXXXXX")
    rmdir "$backup"
    mv "$target" "$backup"
  fi
  mv "$stage" "$target"
  stage=''
  printf 'Installed: %s\n' "$target"
  if [ -n "$backup" ]; then printf 'Previous copy backed up: %s\n' "$backup"; fi
  backup=''
done
printf 'Done. Start a new agent session in your project.\n'
