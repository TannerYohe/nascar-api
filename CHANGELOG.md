# CHANGELOG


## v0.1.1 (2026-05-26)

### Bug Fixes

- Use RELEASE_TOKEN to bypass branch protection in release workflow
  ([#5](https://github.com/TannerYohe/nascar-api/pull/5),
  [`ef55dcd`](https://github.com/TannerYohe/nascar-api/commit/ef55dcdb4a118f3311ff95998648241843f0cf13))

- **ci**: Split release workflow into separate build and publish jobs
  ([`0aa2836`](https://github.com/TannerYohe/nascar-api/commit/0aa28361baaf01fa75bfaa7f6e2b6de35a993eb7))

fix(ci): split release workflow into separate build and publish jobs

- **ci**: Split release workflow into separate build and publish jobs
  ([`b5bc126`](https://github.com/TannerYohe/nascar-api/commit/b5bc126f3fd0c30835a676f6280ae0b832f7cf9f))

The publish job now checks out the tagged commit directly, ensuring poetry-dynamic-versioning picks
  up the correct version from the git tag rather than relying on Docker container workspace state.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

### Continuous Integration

- Use RELEASE_TOKEN to bypass branch protection in release workflow
  ([`9e2214a`](https://github.com/TannerYohe/nascar-api/commit/9e2214ae9b5ff39324db323514ea4f2a4f4e47f0))

GITHUB_TOKEN cannot push directly to main when branch protection requires pull requests. Use a PAT
  stored as RELEASE_TOKEN instead.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>


## v0.1.0 (2026-05-26)

### Features

- Prepare package for public release
  ([`4749776`](https://github.com/TannerYohe/nascar-api/commit/47497767e63bde9c52c97d810f789229b1fbd8aa))
