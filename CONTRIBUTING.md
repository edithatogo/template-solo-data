# Contributing

## Development

Use Python 3.15.1 to reproduce the current pinned CI. The package manifest allows Python 3.14 or newer. Create an isolated environment from the repository root:

```sh
python3.15 -m venv .venv
.venv/bin/python -m pip install -e ".[test]"
```

On Windows, use `.venv\Scripts\python.exe` for the environment's Python commands.

Use four-space Python indentation. Prefer synthetic or appropriately licensed test fixtures. Document each input's origin, rights and checksum in `data/README.md`. Configure logging only at the pipeline entry point, and never include source records, credentials or direct personal data in logs.

See [BOOTSTRAP.md](BOOTSTRAP.md) when creating a new project from this starter.

## Validation

```sh
.venv/bin/python -m pytest --cov --cov-report=xml
```

This includes the structured-logging regression and creates real executable coverage. Record data validation, source rights, checksums and publication evidence separately; passing code tests does not establish those properties. CI additionally uploads coverage through Codecov OIDC.

Record the command, tool versions and outcome in the pull request. Distinguish
passed, failed, skipped and unavailable checks; include a hosted run link when
available. Required automated checks must pass before integration.

## Pull requests

Use a focused branch such as `fix/short-summary`, `feat/short-summary` or
`docs/short-summary`. Explain the problem and resulting behaviour, link related
issues, and include the validation evidence. Keep commits reviewable and update
affected documentation, examples and tests with the change. Identify any
compatibility, generated-output, release or data impact.

The repository has one maintainer. Automated review and required checks replace
mandatory human approval; do not add a second-reviewer, team or CODEOWNERS gate.
Preserve unrelated work and existing security/publication requirements.

## Security and support

Use the repository's issue chooser for reproducible bugs or scoped proposals.
For usage questions, include a minimal safe example and what you have already
tried. Follow [SECURITY.md](SECURITY.md) for vulnerabilities; do not put private
data, credentials or sensitive exploit details in public issues or logs.

Follow the account's
[code of conduct](https://github.com/edithatogo/.github/blob/main/CODE_OF_CONDUCT.md).
When adopting this template under a different owner, replace this link with the
new project's policy and verify its support and private-reporting routes.
