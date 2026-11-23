<!--
Theme add/update PR template.
PR title format: type(scope): subject [TICKET-ID], for example "feat(theme-mono): add Mono official theme [LTH-001]".
Co-authored-by trailers are allowed; contributors still commit under their own identity.
Submitting here is optional: you can publish from your own Git repository or as a .glint file without any review from us.
-->

**Ticket:** <!-- Stable ticket ID (LTH-NNN or LCOM-NNN) or "new community submission". -->

## Theme

- Package ID (unique, e.g. `community.my-theme`):
- Version (SemVer):
- Author and attribution:
- Upstream source repository and tag or commit:

## Submission checklist

- [ ] `glint.json` validates against the supported manifest schema version.
- [ ] Declared `requiredCapabilities` and optional features match what the theme actually uses.
- [ ] Platform claims (Windows / Linux / macOS) reflect tested environments or documented fallbacks.
- [ ] All runtime assets are bundled; the theme works offline by default.
- [ ] No install scripts, native binaries, or network-loaded executable JavaScript.
- [ ] Every font, icon, image, and sound has a declared license and attribution; nothing proprietary or trademarked without rights.
- [ ] Screenshots show the real running Glint surface, not misleading OS-native screenshots.
- [ ] Keyboard, labels, contrast, and reduced-motion behavior were checked.
- [ ] Package size is within the published limit (see CONTRIBUTING.md).
- [ ] Changelog, known limitations, and rollback guidance are included.
- [ ] This theme is not presented as created by the Glint maintainers unless it is.

## Verified environments

<!-- OS build, session/compositor, WebView runtime, GPU/driver, Glint version. List only what you actually tested. -->

## Licenses

<!-- Theme code license plus a table of asset and font licenses. -->
