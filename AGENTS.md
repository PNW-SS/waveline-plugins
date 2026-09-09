# Working on Waveline plugins

- Keep this repository focused on plugin manifests, assets, setup documentation,
  validation, and packaging. MCP/OAuth, access control, sends, and billing belong
  to the application repositories and are not duplicated here.
- Each environment has a fixed MCP URL. Keep both platform manifests at the
  shared `VERSION`, and update `environments.json` with any intentional URL change.
- Do not add credentials, invented app IDs, authentication bypasses, or install
  hooks. Hosted registrations must exist before adding their binding files.
- Local-only environment variables must start with `LOCAL_ONLY_`. Keep them
  optional in required-variable validation and out of deployed settings.
- Run `python scripts/package.py validate`, `python -m unittest discover -s tests -v`,
  and `python scripts/package.py build` after package changes. Run Claude's strict
  validator for changed Claude manifests and marketplace entries when available.
- Package validation is not live OAuth verification or directory approval.
  Report remaining registration and backend prerequisites accurately.
- Do not commit, push, publish a release, install a plugin, or change account
  settings unless the user requests it.
