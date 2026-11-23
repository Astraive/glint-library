# Changelog

All notable changes to this repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and future releases will follow [VERSIONING.md](VERSIONING.md).

## [Unreleased]

**Repository status:** foundation only. **No themes, `registry.json`, theme-validation workflow, or release tag exists yet.**

### Added

- Repository foundation (`[LIB-001]`): MIT license, README, CONTRIBUTING, SECURITY, SUPPORT, GOVERNANCE, CODE_OF_CONDUCT, VERSIONING, `.editorconfig`, `.gitattributes`, `.gitignore`.
- Opt-in local Git hooks ([.githooks/README.md](.githooks/README.md)) and read-only checks (`scripts/check-repository.py`, `scripts/check-conventions.py`, `scripts/check-powershell.ps1`).
- GitHub configuration: CODEOWNERS, Dependabot, release notes categories, issue forms (theme submission, bug, task), pull request templates (default, theme, registry), and the `repository-checks` and `security-analysis` workflows.
