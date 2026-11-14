# Solo-maintainer data pipeline template

[![CI](../../actions/workflows/ci.yml/badge.svg)](../../actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Citation](https://img.shields.io/badge/citation-CFF-blue.svg)](CITATION.cff) [![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/edithatogo/template-solo-data/badge)](https://securityscorecards.dev/viewer/?uri=github.com/edithatogo/template-solo-data)

A Python 3.14 data-pipeline baseline with provenance controls, reusable CI, real coverage, structured logging, Renovate, and tag-derived versions.

## Status

This repository is designed for one maintainer. Automated checks are required;
no second reviewer, CODEOWNERS approval, team membership, or mandatory human
approval is introduced.

## Usage

Choose **Use this template** to create a Python data project, then follow the
[adoption checklist](BOOTSTRAP.md). The starter supplies a package skeleton,
a structured-logging helper and tests. Add the actual collection or
transformation logic with synthetic or rights-cleared fixtures.

1. Replace `replace-me-data` in `pyproject.toml` and rename
   `src/replace_me_data/`; update imports and the generated-version path.
2. Document each input's origin, rights and checksum in `data/README.md`.
3. Follow [CONTRIBUTING.md](CONTRIBUTING.md) to create an environment matching
   the current CI, then install with `python -m pip install -e ".[test]"`.
4. Run `python -m pytest --cov --cov-report=xml` and review the generated
   coverage alongside the separate data-governance evidence.

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup and validation commands, and
[BOOTSTRAP.md](BOOTSTRAP.md) for the adoption checklist.

The pinned shared CI runs executable tests and creates coverage output; its
Codecov upload requires separate provider activation and observed execution.
Data validity, rights, provenance, checksums and publication remain separate
evidence.

## Versioning

The pipeline package version is derived from Git tags by `hatch-vcs`. Dataset releases also require immutable checksums and, where applicable, DOI deposit metadata.

## Logging

Use `replace_me_data.logging.configure_logging` at the pipeline entry point. JSON logs include safe event context and run identifiers; never log source records, credentials, or direct personal data.

## Security

Follow [SECURITY.md](SECURITY.md) for private reporting and the safe contact
fallback if GitHub's **Report a vulnerability** option is unavailable. Do not
include credentials, sensitive source data or exploit details in public issues.

## Citation

See [CITATION.cff](CITATION.cff). Release-specific versions and identifiers are
added only when the release exists.

## License

Repository-authored starter material is MIT licensed; see [LICENSE](LICENSE).
Record third-party and source-data rights separately.
