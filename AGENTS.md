# Working on Waveline plugins

- Keep this public repository focused on the production plugin, customer setup
  instructions, branding, validation, and packaging.
- Keep internal runbooks, deployment details, test-account information, and
  non-production configurations outside this repository.
- Keep both platform manifests aligned with `VERSION` and the production URL in
  `environments.json`.
- Never add credentials, invented app IDs, authentication bypasses, or install hooks.
- Run `python scripts/package.py validate`,
  `python -m unittest discover -s tests -v`, and
  `python scripts/package.py build` after package changes. Run Claude's strict
  validator for changed Claude manifests and marketplace entries when available.
- Package validation is not live OAuth verification or directory approval.
- Do not commit, push, publish a release, install a plugin, or change account
  settings unless the user requests it.
