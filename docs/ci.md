# CI and releases

The GitHub Actions workflow is ready in `.github/workflows/plugins.yml`. It runs
on pull requests, pushes to `develop`, `staging`, `alpha`, and `main`, version tags,
and manual dispatch. It needs
no Waveline, OpenAI, or Anthropic credentials and makes no MCP requests.

The validation job checks both manifests and marketplaces, fixed environment
URLs, asset containment, versions, and credential-free MCP configurations. It
runs regression tests and the pinned Claude CLI's strict validator, builds eight
ZIPs, and uploads the ZIPs and checksums as a 14-day workflow artifact. The
OpenAI checks are repository-owned checks for the supported manifest subset;
they are not an OpenAI store approval or a replacement for hosted review.

Action revisions and the Claude CLI version are pinned. Update them explicitly
and rerun local and CI checks when platform packaging requirements change.

## GitHub and branch rules

The private repository is `PNW-SS/waveline-plugins`, with `develop` as its default
branch. Its permanent branches are `develop`, `staging`, `alpha`, and `main`,
matching the Waveline web, database, and Cloudflare repositories. The local
checkout is an independent Git repository alongside those repositories.

All four branches have active rulesets requiring pull requests, one approving
review, stale-review dismissal, and approval after the last push. Force pushes
and branch deletion are blocked. The `pnw-admin` team has the same pull-request
bypass as the reference repositories, and its approval is specifically required
for `alpha` and `main`. Extra approval for unattributed changes is enabled.

Required GitHub Actions checks are `enforce-flow` and `Validate and build`.
The branch-flow workflow permits any source into `develop`, then only
`develop -> staging -> alpha -> main`. The plugin build replaces the other
repositories' application-specific build/test checks. No Supabase or app
deployment checks are required by this repository.

Keep the repository private while reviewing development environment metadata.
The server-side rulesets must be maintained in GitHub; changing workflow YAML
alone does not change branch protection.

## Versioned releases

1. Change `VERSION` and all eight platform manifests to the same x.y.z version.
2. Update `docs/release-notes.md` with the actual changes and known limitations.
3. Run validation/tests/build and review the pull request into `develop`, then
   promote through `staging`, `alpha`, and `main` using pull requests.
4. After promotion to `main`, tag that reviewed commit `v` followed by the exact version.
5. Pushing the tag runs validation again and creates a **draft GitHub release**
   containing only the two production ZIPs and their checksums. Review the draft
   before publishing. If a draft already exists, the create step fails rather
   than overwriting its artifacts; review the existing draft before retrying.

The release job alone receives `contents: write`; normal validation is read-only.
GitHub's built-in workflow token is sufficient. ZIPs for Alpha, Staging, and Local
stay in the CI artifact and are not attached to the draft release. Public source
still exposes committed files, so release filtering is not a privacy boundary.

CI creates no public store listing and does not deploy the MCP server. Complete
platform registration, legal/support metadata, review fixtures, native OAuth
compatibility, and hosted testing before submission. Backend changes must pass
the backend repositories' own tests; package CI cannot verify billing or access
control behavior remotely.
