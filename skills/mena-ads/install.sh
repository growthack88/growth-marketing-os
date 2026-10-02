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
  # claude.ai accepts descriptions up to 200 characters; Claude Code and the API
  # accept 1,024. The zip carries a short description, the folder keeps the long one.
  out="$(pwd)/mena-ads.zip"
  tmp="$(mktemp -d)"
  cp -R "$SKILLS_ROOT/mena-ads" "$tmp/mena-ads"
  rm -f "$tmp/mena-ads/install.sh"
  python3 - "$tmp/mena-ads/SKILL.md" <<'PY'
import re, sys
path = sys.argv[1]
text = open(path, encoding="utf-8").read()
short = ("Paid-ads skill for the Arab world: audits, media plans, scale/kill calls, Arabic ad copy, "
         "tracking and COD real ROAS on Meta, Google, TikTok, Snapchat. إعلانات وحملات")
assert len(short) <= 200
text = re.sub(r"description: >\n(?:  .*\n)+", f"description: \"{short}\"\n", text, count=1)
open(path, "w", encoding="utf-8").write(text)
PY
  rm -f "$out"
  (cd "$tmp" && zip -qr "$out" mena-ads -x "*/.DS_Store")
  rm -rf "$tmp"
  echo "Built $out — upload it in the Claude app: Customize → Skills → + → Create skill → Upload a skill"
  echo "(turn on Settings → Capabilities → Code execution first)."
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
