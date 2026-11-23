# Contributing to Glint Library

Thank you for contributing to `Astraive/glint-library`. Read [README.md](README.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) first. Application, SDK, package-format, and runtime changes belong in [`Astraive/Glint`](https://github.com/Astraive/Glint).

## Repository stage and scope

This repository is at its **foundation stage**: no themes, no `registry.json`, and no theme-validation workflows exist yet. Do not add placeholder themes, an empty registry, or no-op workflow stubs. Those arrive through the catalog and theme tickets (`CAT`, `LTH`, `LQA`). Every change must state truthfully what was verified and what remains unimplemented.

## Submitting is optional

You do not need to submit here to publish a Glint theme. You can host it in your own Git repository, run your own registry, or share a `.glint` file. This library is an optional, curated discovery channel.

## Theme submission rules

These come from the Glint plan for community publishing and apply once intake opens. A submission must meet all of the following:

- A unique package ID, a SemVer version, and an explicit author and license.
- `glint.json` validates against a supported manifest schema version.
- Every published surface entrypoint is built and locally tested. CI will rebuild in a clean environment and compare digests.
- `requiredCapabilities` and optional features are declared accurately.
- Windows, Linux, and macOS claims reflect real tests or clearly documented fallbacks. List the environment tuples you tested.
- All runtime assets are bundled and the theme works offline by default.
- No install scripts, no native binaries, and no network-loaded executable JavaScript. No restricted-API use or remote script references.
- Every image, font, icon, and sound has a declared license and attribution, and total package size is within the published limit. Proprietary or trademarked assets are rejected without verified rights.
- Screenshots and previews show the actual running Glint surface, not misleading OS-native screenshots.
- Accessibility is checked: keyboard use, labels, contrast, and reduced motion.
- A changelog, known limitations, update origin, and rollback guidance are included.
- Signed tags or packages where a supported signing scheme exists.
- Themes are never presented as made by the Glint maintainers unless they are. The terms `featured`, `official`, and `verified` have defined meanings and are assigned only by maintainers.

Review includes automated manifest, build, static-audit, license, size, and preview checks, plus a manual review of quality, security, and misleading claims. The generated registry index and package digests are produced by CI. Do not hand-edit them. Removal of malicious or infringing themes follows [SECURITY.md](SECURITY.md) and [GOVERNANCE.md](GOVERNANCE.md).

## Prerequisites and local verification

Python 3.12+ (standard library only), PowerShell 7 (`pwsh`), and Git:

```sh
python scripts/check-repository.py
python scripts/check-conventions.py --title "docs(repo): clarify policy links [LIB-001]"
pwsh -NoProfile -File scripts/check-powershell.ps1
```

Opt-in hooks ([.githooks/README.md](.githooks/README.md)) are installed with `pwsh -NoProfile -File .githooks/install.ps1`. They set only the repository-local `core.hooksPath` and never touch your global Git configuration or identity.

## Commit messages and PR titles

Pull requests are squash-merged, so the PR title becomes the commit subject on `main`. Subjects must match:

```text
type(scope): subject [TICKET-ID]
```

- **Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
- **Scope:** lowercase kebab-case matching `^[a-z0-9][a-z0-9-]*$`, for example `repo`, `ci`, `registry`, `theme-mono`.
- **Ticket ID:** matching `[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+`. Library prefixes are `LIB` (foundation), `CAT` (catalog and registry index), `LTH` (official themes), `LCOM` (community), `LLEG` (licensing), `LQA` (library quality), and `LREL` (library release). Dependency PRs use `REL-009`.
- **`Co-authored-by:` trailers are allowed.** Each contributor still commits under their own identity.
- **No Dependabot bypass:** the maintainer renames automatic dependency PRs to include `[REL-009]` before merge.

Issue conventions, labels, and milestones are defined in the [`Astraive/Glint` issue conventions](https://github.com/Astraive/Glint/blob/main/docs/issue-conventions.md).

## External backlog boundary

Detailed backlog records live outside Git. Never copy `.issues/`, `issue.json`, publication ledgers, or reports into this repository, and never invent GitHub issue numbers before authorized publication.

## Privacy and rights

Never commit personal media, tokens, secrets, unredacted host paths, or fonts, icons, and images without a verified license. Report security problems privately per [SECURITY.md](SECURITY.md).
