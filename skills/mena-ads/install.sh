#!/usr/bin/env bash
# Install the MENA Ads skill (plus its companion skills) into any agent that reads SKILL.md folders.
#
#   ./install.sh                 → Claude Code, personal (~/.claude/skills)
#   ./install.sh --project       → Claude Code, this project only (./.claude/skills)
#   ./install.sh --dir PATH      → any other skills folder (Codex, Gemini CLI, Cursor, OpenCode, your own agent)
#   ./install.sh --zip           → build mena-ads.zip to upload in Claude.ai → Settings → Capabilities → Skills
#
# Companion skills (installed alongside, linked from inside the skill):
#   cod-operations-analyst · arabic-copy-localizer · performance-media-buyer · benchmark-analyst
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_ROOT="$(cd "$HERE/.." && pwd)"
COMPANIONS=(cod-operations-analyst arabic-copy-localizer performance-media-buyer benchmark-analyst)

target="$HOME/.claude/skills"
mode="copy"
case "${1:-}" in
  "" ) ;;
  --project ) target="$(pwd)/.claude/skills" ;;
  --dir ) target="${2:?usage: ./install.sh --dir PATH}" ;;
  --zip ) mode="zip" ;;
  -h|--help ) sed -n '2,10p' "$0"; exit 0 ;;
  * ) echo "Unknown option: $1 (try --help)"; exit 1 ;;
esac

if [ "$mode" = "zip" ]; then
  out="$(pwd)/mena-ads.zip"
  rm -f "$out"
  (cd "$SKILLS_ROOT" && zip -qr "$out" mena-ads -x "*/.DS_Store" "mena-ads/install.sh")
  echo "Built $out — upload it in Claude.ai (Settings → Capabilities → Skills)."
  exit 0
fi

mkdir -p "$target"
for s in mena-ads "${COMPANIONS[@]}"; do
  if [ -d "$SKILLS_ROOT/$s" ]; then
    rm -rf "${target:?}/$s"
    cp -R "$SKILLS_ROOT/$s" "$target/$s"
    echo "  ✓ $s → $target/$s"
  fi
done
chmod +x "$target/mena-ads/scripts/ads_calc.py" 2>/dev/null || true
echo
echo "Done. Start a new session and type:  /mena-ads   (or just ask: \"audit my Meta account\" / \"راجع حملاتي\")"
