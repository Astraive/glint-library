# Governance

## Governance model

`Astraive/glint-library` operates under a **single-maintainer bootstrap model** led by organization owner and repository administrator **`@NeerajCodz`** (`https://github.com/NeerajCodz`). It is a companion to [`Astraive/Glint`](https://github.com/Astraive/Glint) with its own policies, license rules, and per-asset provenance records.

## Roles

### Maintainer (`@NeerajCodz`)

- Owns repository settings, branch protection, CI trust boundaries, and final merge authority on `main`.
- Signs off on library gates `LQA-L0` through `LQA-L3` and never waives destructive-data, archive-escape, permission-bypass, or supply-chain failures.
- Triages private reports under [SECURITY.md](SECURITY.md), enforces [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and decides takedowns of malicious or infringing themes.
- Alone assigns the labels `featured`, `official`, and `verified`, which have defined meanings and are never self-declared by authors.

### Contributors

- Submit scoped changes per [CONTRIBUTING.md](CONTRIBUTING.md) with truthful verification evidence and updated documentation.

## Not a gatekeeper

The library is Glint's default registry source but never the only permitted one. Independent Git repositories, custom registries, and standalone `.glint` files remain first class. Nothing in this repository may make it a requirement for publishing themes.

## Review policy

- `main` is protected: pull requests, squash merges, linear history, resolved conversations, and required passing CI checks.
- **Dependabot triage:** CI enforces the `type(scope): subject [TICKET-ID]` title with no bot bypass. The maintainer renames automatic dependency PRs to include `[REL-009]` before merge.
- **Bootstrap exception:** a sole maintainer cannot approve their own PRs, so required approvals are `0` during bootstrap. PRs must still satisfy `.github/CODEOWNERS`, the PR checklist, and required CI. Approvals increase to at least 1 once additional trusted maintainers hold write access.
- Workflow, registry-generation, and licensing changes receive explicit security review.

## Licensing and asset provenance

Repository code, scripts, and documentation are MIT licensed ([LICENSE](LICENSE)). **Each theme declares its own asset, font, and icon licenses**, and those licenses may differ from the repository license. A theme is accepted only if its declared licenses permit redistribution through the library; unverified or proprietary assets are rejected. A contribution agreement and the license for official themes are open decisions in the Glint plan and are not settled here.

## Changes to governance

Changes to registry semantics, trust levels, or takedown policy are recorded in [CHANGELOG.md](CHANGELOG.md) and coordinated with the Glint decision register in `Astraive/Glint`.
