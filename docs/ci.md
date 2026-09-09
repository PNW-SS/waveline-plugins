# CI and releases

CI validates the production manifests, marketplace entries, MCP configuration,
assets, and version. It runs packaging tests and Claude's strict validator,
then builds two production ZIPs with SHA-256 checksums.

Run the same checks locally:

```sh
python scripts/package.py validate
python -m unittest discover -s tests -v
claude plugin validate --strict plugins/waveline
claude plugin validate --strict .claude-plugin/marketplace.json
python scripts/package.py build
```

The workflows use pinned actions and a pinned Claude CLI. Ordinary validation
uses a read-only GitHub token and does not connect to Waveline or require account
credentials. Package validation does not verify the live service.

## Release

1. Keep `VERSION` and both plugin manifests at the same stable x.y.z version.
2. Update `docs/release-notes.md` with the user-visible changes and limitations.
3. Complete the repository's required review and CI checks.
4. Tag the reviewed release commit with `v` followed by its version.
5. The tag workflow creates a draft GitHub release with the two production
   archives and checksums. Review the draft before publishing it.

The release job uses GitHub's built-in workflow token. Never add customer
credentials, access tokens, operator documentation, or non-production packages
to release artifacts. Directory submission and live service testing are
separate from this build workflow.
