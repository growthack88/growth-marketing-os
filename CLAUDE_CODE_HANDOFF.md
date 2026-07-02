# 🤖 Claude Code Handoff — Growth Marketing OS

> **Mission:** Take this scaffold, initialize it as a git repo, create the GitHub repository, configure it for SEO/GEO, push, and verify. Then (Phase B, on request) generate the first asset batch.

**Owner:** Mahmoud Omar · GitHub: `growthack88` · Brand: "Growth Marketing OS | Mahmoud Omar"
**Repo slug:** `growth-marketing-os` · **Visibility:** public · **License:** MIT (already in repo)

---

## Context (read first)

This folder is a ready-made scaffold for an open-source library of ORIGINAL marketing assets (prompts, Claude skills, agents, n8n workflows, playbooks) — not an awesome-list of links. Key files:

- `README.md` — main page, already branded. Do not rewrite the copy.
- `HOW-TO-USE.md` — beginner/intermediate/advanced paths.
- `templates/ASSET_TEMPLATE.md` — the mandatory anatomy for every asset.
- `_brand/FOOTER.md` — the branding block appended to every asset file.
- `llms.txt` — GEO file for LLM crawlers. Keep in root, keep updated.
- `SETUP-SEO-GEO.md` — maintainer checklist (some items are manual/web-UI).
- 6 sample assets across `prompts/`, `skills/`, `agents/`, `swipe-files/`, `workflows/` — these define the quality bar.

## Phase A — Ship the repo (do now)

1. **Sanity pass (no rewriting):**
   - Verify every internal link in README.md, HOW-TO-USE.md, prompts/README.md and all "Related assets" sections resolves to a real file. Fix broken paths only.
   - Verify every file that should carry the brand footer has it (all asset files; not LICENSE/llms.txt).
   - Confirm zero remaining `YOUR_GITHUB_USERNAME` or `[bracket]` placeholders outside template files.

2. **Git init + first commit:**
   ```bash
   git init -b main
   git add -A
   git commit -m "feat: Growth Marketing OS v0.1 — scaffold, templates, first 6 assets"
   ```

3. **Create GitHub repo (gh CLI, authenticated as growthack88):**
   ```bash
   gh repo create growthack88/growth-marketing-os --public \
     --description "Growth Marketing OS | Mahmoud Omar — open-source AI marketing prompts, Claude skills, agents & growth playbooks (EN + AR)" \
     --homepage "https://mahmoudomar.com" --source . --push
   ```

4. **Configure topics:**
   ```bash
   gh repo edit growthack88/growth-marketing-os --add-topic marketing --add-topic growth-hacking \
     --add-topic ai-marketing --add-topic prompts --add-topic prompt-engineering --add-topic claude-skills \
     --add-topic chatgpt-prompts --add-topic custom-gpt --add-topic mcp --add-topic n8n \
     --add-topic marketing-automation --add-topic seo --add-topic geo --add-topic paid-ads \
     --add-topic meta-ads --add-topic cro --add-topic arabic --add-topic mena --add-topic growth
   ```

5. **Verify & report:** confirm the repo renders correctly (README badges, tables, links), then output the repo URL + a checklist of the manual items Mahmoud must do in the web UI: social preview image (1280×640), pin repo on profile, enable Discussions.

### Guardrails
- ❌ Do NOT rewrite, "improve," or restyle existing content — the voice is intentional.
- ❌ Do NOT publish anything beyond creating this repo (no posts, no PRs to other repos).
- ❌ Do NOT commit secrets, tokens, or local paths.
- ✅ If `gh` is not authenticated, stop and ask Mahmoud to run `gh auth login` — never handle credentials yourself.

## Phase B — Asset factory (only when Mahmoud says go)

Generate new assets in batches of 5-10. Hard rules:

1. Every asset = one `.md` file following `templates/ASSET_TEMPLATE.md` EXACTLY — all frontmatter fields filled, including `hook`, `email_subject`, `short_pitch` (these feed the n8n content flywheel).
2. Filename = kebab-case, keyword-first: `google-ads-search-terms-audit.md`.
3. **"When I use it" must be a real, specific scenario** — Mahmoud supplies these or approves drafts. Never invent client results or numbers.
4. Append `_brand/FOOTER.md` to every asset.
5. Add 2-3 internal links in "Related assets"; update the parent folder README index.
6. Bilingual assets: Egyptian Arabic (عامية + English business terms code-switching), never فصحى, never literal translation.
7. Commit convention: `feat(prompts): add google-ads-search-terms-audit` — one asset per commit (each commit triggers one content-flywheel run).
8. After each batch: update `llms.txt` section list if new categories appeared.

## Definition of done (Phase A)
- [ ] Repo live at github.com/growthack88/growth-marketing-os
- [ ] README renders clean, all links work
- [ ] Description + homepage + 19 topics set
- [ ] Report delivered with URL + manual to-do list
