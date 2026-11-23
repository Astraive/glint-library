<!--
Pull request template for Astraive/glint-library.
Rules: CONTRIBUTING.md.
PR title MUST match: type(scope): subject [TICKET-ID]
  Allowed types: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert
  Scope: lowercase kebab-case (e.g. repo, ci, registry, theme-mono)
  Ticket ID: library prefixes LIB, CAT, LTH, LCOM, LLEG, LQA, LREL (e.g. [LIB-001], [LTH-001])
PRs are squash-merged into main, so the PR title becomes the commit subject.
Co-authored-by trailers are allowed; contributors still commit under their own identity.
Dependabot PRs have no CI title bypass: maintainers rename them to append [REL-009] before merge.
Specialized templates: ?template=theme.md (theme add/update) and ?template=registry.md (registry, schema, CI).
-->

**Ticket:** <!-- Stable ticket ID (e.g. LIB-001). Add `Closes #N` / `Refs #N` only once the issue is published; do not invent numbers. -->

## What and why

<!-- Summarize the change and which planning contract (Astraive/Glint docs/plan/05-distribution) it implements. -->

## Acceptance criteria

- [ ]

## Test evidence

<!-- Exact commands run and observed results (python scripts/check-repository.py, python scripts/check-conventions.py --title "...", pwsh -NoProfile -File scripts/check-powershell.ps1). Never claim unrun checks passed. -->

## Checklist

- [ ] Only actually executed checks are claimed.
- [ ] No secrets, tokens, personal media, unredacted local paths, or external `.issues/` backlog files are included.
- [ ] Any added asset, font, icon, or fixture has a verified license and attribution.
- [ ] Independence is preserved: nothing makes the official library the only way to distribute Glint themes.
