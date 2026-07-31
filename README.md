# Solo-maintainer data pipeline template

[![CI](../../actions/workflows/ci.yml/badge.svg)](../../actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Citation](https://img.shields.io/badge/citation-CFF-blue.svg)](CITATION.cff)

A Python 3.14 data-pipeline baseline with provenance controls, reusable CI, real coverage, structured logging, Renovate, and tag-derived versions.

## Status

This repository is designed for one maintainer. Automated checks are required;
no second reviewer, CODEOWNERS approval, team membership, or mandatory human
approval is introduced.

## Start here

1. Replace `replace-me-data` and `src/replace_me_data`.
2. Document every input under `data/README.md`.
3. Run `python -m pip install -e ".[test]"`.
4. Run `python -m pytest --cov`.

## Development

CI tests executable transformations and uploads real coverage. Data validity, rights, provenance, checksums, and publication gates remain separate evidence.

## Versioning

The pipeline package version is derived from Git tags by `hatch-vcs`. Dataset releases also require immutable checksums and, where applicable, DOI deposit metadata.

## Logging

Use `replace_me_data.logging.configure_logging` at the pipeline entry point. JSON logs include safe event context and run identifiers; never log source records, credentials, or direct personal data.

## Security

Report vulnerabilities privately through GitHub Security Advisories. See
[SECURITY.md](SECURITY.md); do not disclose credentials or sensitive source data
in a public issue.

## Citation

See [CITATION.cff](CITATION.cff). Release-specific versions and identifiers are
added only when the release exists.

## License

Repository-authored starter material is MIT licensed; see [LICENSE](LICENSE).
Record third-party and source-data rights separately.