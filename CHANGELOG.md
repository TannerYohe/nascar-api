# CHANGELOG


## v0.1.2 (2026-09-23)

### Bug Fixes

- Skip lap notes whose FlagState is not a flag
  ([`ee6173c`](https://github.com/TannerYohe/nascar-api/commit/ee6173cc97dcd208088778dee4cc6bbd0020f559))

lap-notes.json uses FlagState 1000 for broadcast trivia ("Stage 2 has gone caution free in the last
  4 races here"). It describes no flag, so the Flag enum rejects it, and a single such note made
  get_lap_notes raise ValidationError for the whole race -- 10 of the first 12 Cup races of 2025.

Notes with an unrecognised FlagState are now skipped and logged at debug level; the rest of the
  race's notes load as before.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

- Skip lap notes whose FlagState is not a flag
  ([#6](https://github.com/TannerYohe/nascar-api/pull/6),
  [`aed9a2b`](https://github.com/TannerYohe/nascar-api/commit/aed9a2b200e24538a5cef2310e1216507b9d6770))


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
