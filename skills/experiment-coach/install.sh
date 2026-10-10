#!/usr/bin/env bash
# Install the Experiment Coach skill (plus its companion skills) into any agent that reads SKILL.md folders.
#
#   ./install.sh                 → Claude Code, personal (~/.claude/skills)
#   ./install.sh --project       → Claude Code, this project only (./.claude/skills)
#   ./install.sh --dir PATH      → any other skills folder (Codex, Gemini CLI, Cursor, OpenCode, your own agent)
#   ./install.sh --zip           → build experiment-coach.zip to upload in the Claude app or a ChatGPT workspace
#
# Companion skills (installed alongside):
#   benchmark-analyst · funnel-decomposition · ab-testing (community, MIT)
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_ROOT="$(cd "$HERE/.." && pwd)"
COMPANIONS=(benchmark-analyst funnel-decomposition community/ab-testing)

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
  # The Claude app accepts descriptions up to 200 characters; Claude Code and the API
  # accept 1,024. The zip carries a short description, the folder keeps the long one.
  out="$(pwd)/experiment-coach.zip"
  tmp="$(mktemp -d)"
  cp -R "$SKILLS_ROOT/experiment-coach" "$tmp/experiment-coach"
  rm -f "$tmp/experiment-coach/install.sh"
  python3 - "$tmp/experiment-coach/SKILL.md" <<'PY'
import re, sys
path = sys.argv[1]
text = open(path, encoding="utf-8").read()
short = ("Validate ideas before launch and run growth experiments: interviews, smoke tests, pre-sales, "
         "sample sizes, A/B readouts, experiment logs. اختبر فكرتك قبل الإطلاق")
assert len(short) <= 200, len(short)
text = re.sub(r"description: >\n(?:  .*\n)+", f"description: \"{short}\"\n", text, count=1)
open(path, "w", encoding="utf-8").write(text)
PY
  rm -f "$out"
  (cd "$tmp" && zip -qr "$out" experiment-coach -x "*/.DS_Store" "*/__pycache__/*")
  rm -rf "$tmp"
  echo "Built $out — upload it in the Claude app: Customize → Skills → + → Create skill → Upload a skill"
  echo "(turn on Settings → Capabilities → Code execution first)."
  exit 0
fi

mkdir -p "$target"
for s in experiment-coach "${COMPANIONS[@]}"; do
  name="$(basename "$s")"
  if [ -d "$SKILLS_ROOT/$s" ]; then
    rm -rf "${target:?}/$name"
    cp -R "$SKILLS_ROOT/$s" "$target/$name"
    echo "  ✓ $name → $target/$name"
  fi
done
chmod +x "$target/experiment-coach/scripts/exp_calc.py" 2>/dev/null || true
echo
echo "Done. Start a new session and type:  /experiment-coach   (or just ask: \"help me validate my idea\" / \"عايز أختبر فكرتي قبل الإطلاق\")"
