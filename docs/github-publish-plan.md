# GitHub Publish Plan

This plan records the publish path for the public OpenClaw use-case package. It started as a staged local package and is now published.

## Current repository

- Public URL: `https://github.com/ulttla/gun-openclaw-use-cases`
- Local path: maintained in the local development workspace
- Current state: synchronized with `origin/main`
- Remote: `https://github.com/ulttla/gun-openclaw-use-cases.git`

## Repository name

`gun-openclaw-use-cases`

This name keeps the portfolio architecture clean: `gunkr.com` presents the broader `AI Engineering Lab`, while GitHub repositories can be split by tool or execution platform.

## Publish and rename sequence used

```bash
# From the local case-study repository
scripts/validate_public_package.py
git status --short
# initial publication happened under the earlier package name
# final public slug was then updated through GitHub repository metadata
```

## Post-publish checks

- GitHub README renders correctly.
- No private files are visible in the repository file tree.
- Repository link is present on gunkr.com under AI Engineering Lab.
- Old GitHub slug redirects to the new repository URL.

## Rollback if published by mistake

If the repo is accidentally published with an issue:

1. Set repository visibility to private immediately.
2. Rotate any exposed credentials if applicable.
3. Remove or rewrite the affected history.
4. Re-publish only after a clean scan.
