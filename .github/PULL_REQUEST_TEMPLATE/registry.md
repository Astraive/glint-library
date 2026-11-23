<!--
Registry, schema, collection, or CI change PR template.
PR title format: type(scope): subject [TICKET-ID], for example "feat(registry): add registry schema v1 [CAT-001]".
-->

**Ticket:** <!-- Stable ticket ID (CAT-, LQA- or LREL-NNN). -->

## What and why

<!-- What changes in registry.json, schemas/, collections/, or workflows, and why. -->

## Checklist

- [ ] The registry schema version changes only with a documented migration (VERSIONING.md).
- [ ] Index fields are generated from theme manifests by CI, not hand-edited; integrity hashes are CI-generated.
- [ ] Registry metadata remains an index; the installed package's `glint.json` still validates independently.
- [ ] Workflow changes use SHA-pinned actions, `permissions: contents: read`, and no `pull_request_target`.
- [ ] Only actually executed checks are claimed below.

## Test evidence

<!-- Exact commands and observed output. -->
