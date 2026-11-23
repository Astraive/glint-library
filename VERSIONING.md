# Versioning Policy

`Astraive/glint-library` versions **independently of the Glint application**. Library content, the registry index schema, and each theme evolve on their own streams, and each declares which Glint contracts it targets. All schema versions below are **proposals from the Glint plan**, not frozen standards.

## Current pre-release status

- **Library releases and registry snapshots:** Unreleased; no tags exist.
- **Registry index schema:** Draft, not frozen; no `registry.json` exists yet.

## Independent version streams

| Stream | Scheme | State | Rule |
| --- | --- | --- | --- |
| Library releases and registry snapshots | Semantic Versioning (`MAJOR.MINOR.PATCH[-prerelease]`) | Unreleased | Tags are cut independently of any Glint app version. |
| Registry index schema | Integer `schemaVersion` | Draft | Versioned independently of the app. Clients reject unknown major versions explicitly. Changes require a documented migration here. |
| Each theme | SemVer in `glint.json` | None yet | A theme version changes whenever its content changes; the index version is generated from the manifest by CI. |
| Targeted Glint contracts | Manifest `schemaVersion`, package format version, SDK `entrypointVersion` | Draft in Glint | Each theme and each registry snapshot declares which of these it targets. Defined by `Astraive/Glint`, see its [VERSIONING.md](https://github.com/Astraive/Glint/blob/main/VERSIONING.md). |

## Rules

1. The registry index is an index only. Index fields are generated from manifests by CI, and an installed package's own `glint.json` must validate independently.
2. A syntactically valid theme can still be incompatible with an older Glint runtime, a platform, or a missing capability. Compatibility is reported, not silently altered.
3. Library releases and schema changes are recorded in [CHANGELOG.md](CHANGELOG.md). Breaking registry schema changes need a migration entry and a new `schemaVersion`.
4. Removing a theme version (takedown) is announced, and installed local copies keep working offline unless users revoke them.
5. Pre-`1.0.0` releases may change draft schemas; the schema freezes only after Glint's client and the library's validators agree at the relevant quality gate.
