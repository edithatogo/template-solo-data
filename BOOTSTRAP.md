# Adopt this template

This checklist applies when creating a project with **Use this template**.
The new repository receives a starter snapshot. Later upstream improvements
need deliberate adoption through reviewed changes.

## Identity and rights

- Rename `replace-me-data` in `pyproject.toml` and `src/replace_me_data/`, then update imports, tests and the generated-version path in both the manifest and `.gitignore`.
- Replace the README title, description, badges and repository/project URLs.
  Check links in community policies and agent instructions as well as manifests.
- Review `CITATION.cff` against the new project's actual title, authors,
  repository and licence. Add no invented DOI, ORCID or release claim.
- Review the existing `LICENSE` and retain required attribution. Record separate
  rights and provenance for imported code, text, data, models, fonts and figures;
  a starter licence does not grant rights over third-party material.

## Development and verification

- Follow [CONTRIBUTING.md](CONTRIBUTING.md) for setup and local validation.
  Record the exact runtime/tool versions and actual outcomes.
- Review the pinned reusable workflow calls against the new project's layout and
  commands. Qualify runtime or action upgrades separately.
- Verify Renovate and any applicable coverage provider in the new repository.
  Copied configuration does not establish provider installation or execution.
- Update `AGENTS.md` with the adopted project's architecture, important paths,
  real validation commands and boundaries. Keep tool-specific adapters aligned.

## Community defaults

- Recheck the issue chooser, PR template and community policies under the new
  owner. Account defaults apply only to repositories owned by that account;
  files inherited on GitHub are not copied into a generated repository or clone.
  Use the new owner's defaults or materialise tailored files when needed.
- A local valid issue template or chooser configuration overrides the entire
  inherited issue-template directory. Include every intended local form and
  verify the chooser after introducing an override.
- Confirm support, conduct and private vulnerability-reporting routes are usable.
  Do not publish sensitive details to test a reporting route.
- Preserve zero mandatory human approvals, automated checks and the existing
  security and publication boundaries.

See GitHub's
[default community-file guidance](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file).

## Environment and containers

This starter requires no application environment variables. A custom devcontainer
is optional; the local toolchain workflow is documented in CONTRIBUTING.

- If environment configuration is introduced, add a safe `.env.example` or
  equivalent documented example. Describe required/optional variables, defaults
  and scope; use placeholders rather than credentials.
- Before adopting a devcontainer, qualify its toolchain and validation commands
  and review its lifecycle commands. Its presence does not enable Codespaces or
  prove that a container build works.
- Update `.github/community-bootstrap.json` when either decision changes.
  Set `template_repository` to `false` for an ordinary generated project, or
  retain `true` only when the project itself is intended as a GitHub template.
  The audit checks GitHub's observed template setting separately.

## Generated files and publication

Python caches, local virtual environments, coverage, packaging outputs and the Hatch-generated version file are ignored. Source data and fixtures are not blanket-ignored: their inclusion requires an explicit rights and privacy decision. Update the generated-version ignore path after renaming the package.

The ignore file is an aid to keeping generated output out of changes; it does
not remove already tracked files or replace privacy and secret scanning.
Keep example environment files tracked and real credentials outside Git.

Build/test success is separate from publication. Configure a release or deployment
only for an intentional destination, verify the resulting artefact or deployed
revision, and keep citation/version information tied to real releases.
