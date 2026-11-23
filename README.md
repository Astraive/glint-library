# Glint Library

`Astraive/glint-library` is the **official public theme library maintained by the Glint team**. It is the companion to the main application repository, [`Astraive/Glint`](https://github.com/Astraive/Glint).

## Status: foundation only

This repository currently contains **repository infrastructure only**: governance and policy files, local Git hooks, read-only check scripts, and GitHub templates and workflows.

- There are **no themes** yet.
- There is **no `registry.json`** yet, and no registry schema has been frozen.
- There are **no theme-validation or registry-build workflows** yet. They will be added with the catalog and quality tickets, not stubbed ahead of time.
- Glint itself is in a planning baseline; no executable app, installer, or published `.glint` package exists.

Nothing here should be read as a shipped catalog. See [CHANGELOG.md](CHANGELOG.md) for exactly what exists.

## This library is optional

The library is Glint's **default** registry source, **not a gatekeeper**. Independent distribution is first class, and no approval from this repository or from the Glint maintainers is needed to publish a theme:

1. **A single-theme Git repository.** Put `glint.json` and the built output at the repository root; users install it by URL and ref.
2. **Your own multi-theme registry.** Host a `registry.json` with theme subfolders and have users add it to Glint.
3. **A portable `.glint` file.** Release it anywhere, share it peer to peer, or install it offline.
4. **An optional submission here** for discovery and curation. See [CONTRIBUTING.md](CONTRIBUTING.md).

These are distribution formats of the same package, not separate runtime types. The package format never depends on this repository's internal tree.

## Planned layout

Taken from the Glint plan (`docs/plan/05-distribution/registry-and-glint-library.md` in `Astraive/Glint`). It is a recommendation, not a frozen contract, and none of it exists yet:

```text
glint-library/
├── registry.json
├── themes/
│   ├── mono/
│   │   ├── glint.json
│   │   ├── dist/
│   │   ├── assets/
│   │   └── preview.png
│   └── carbon/
├── collections/
│   ├── featured.json
│   └── minimal.json
├── previews/
├── schemas/
├── scripts/
└── .github/workflows/
    ├── validate-themes.yml
    └── build-registry.yml
```

If the library grows large, prebuilt `.glint` release assets or sharded registries may replace in-tree builds to avoid bloating Git history. Registry metadata is an **index**: an installed package's own `glint.json` must still validate independently, and CI is meant to generate index fields and integrity hashes from manifests rather than hand-editing them.

## Licensing

Repository code and documentation are MIT licensed ([LICENSE](LICENSE)). **Each theme declares its own asset, font, and icon licenses**; the MIT license of this repository does not automatically cover them. See [GOVERNANCE.md](GOVERNANCE.md).

## Project management

Labels, milestones, and the GitHub Project (`Glint — Master Development Roadmap`) are defined in the **`Astraive/Glint`** repository only, under `.github/project-management/`. Its `configure-github.ps1` script manages both repositories. Library tickets use the prefixes `LIB`, `CAT`, `LTH`, `LCOM`, `LLEG`, `LQA`, and `LREL`, and library milestones are `L0` to `L3`. Detailed backlog records live outside Git.

## Local checks

Python 3.12+ (standard library only), PowerShell 7, and Git:

```sh
python scripts/check-repository.py
python scripts/check-conventions.py --title "docs(repo): clarify policy links [LIB-001]"
pwsh -NoProfile -File scripts/check-powershell.ps1
```

Opt-in local hooks are described in [.githooks/README.md](.githooks/README.md).

## Policies

- [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), [SECURITY.md](SECURITY.md), [SUPPORT.md](SUPPORT.md), [VERSIONING.md](VERSIONING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
