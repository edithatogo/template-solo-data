# AGENTS.md

## Repository map

- `pyproject.toml`: package identity, Python floor, test extra and Hatch/VCS version source.
- `src/replace_me_data/`: pipeline starter and opt-in structured logging.
- `tests/`: transformation/logging tests.
- `data/README.md`: input provenance and rights requirements.
- `.github/workflows/ci.yml`: pinned shared data CI caller.

## Development and validation

Read [CONTRIBUTING.md](CONTRIBUTING.md) for the required setup, exact local
commands and evidence requirements. Use the documented Python environment and run pytest with coverage; preserve the separate hosted coverage gate.
Package versions come from `hatch-vcs` release tags. Dataset versions, checksums, rights and deposits require their own evidenced records.

## Operating model

This repository is maintained by one developer. Automated review, tests and
security gates replace mandatory human approvals. Do not add CODEOWNERS approval
requirements, team assignments or a second-maintainer dependency. Use a focused
branch and reviewable pull request; preserve unrelated and unmerged work.

## Boundaries

Never commit credentials or sensitive data. Keep generated files reproducible.
Prefer one authoritative configuration and link to it from tool-specific files.
Use synthetic or rights-cleared fixtures. Keep source-record values and direct
personal data out of logs. Data/privacy/publication acceptance remains separate
from passing transformation tests.

Use [BOOTSTRAP.md](BOOTSTRAP.md) for adoption decisions. Keep the applicability
declarations in `.github/community-bootstrap.json` aligned with actual project
configuration; they do not substitute for observed GitHub settings.
