# GitHub Publish Plan

This plan is intentionally staged. It prepares a public-ready package without making the repository public until the final approval gate.

## Current local repository

- Local path: project folder under the local development workspace
- Current state: clean-history draft with one public-facing commit
- Remote: not required until approval

## Recommended repository name

`gun-openclaw-use-cases`

## Publish steps after approval

```bash
# From the local case-study repository
scripts/validate_public_package.py
git status --short
gh repo create ulttla/gun-openclaw-use-cases --public --source=. --remote=origin --push
```

## Post-publish checks

- GitHub README renders correctly.
- Mermaid diagrams render or are converted to static images if needed.
- No private files are visible in the repository file tree.
- Repository link is added to gunkr.com only after final content review.

## Rollback if published by mistake

If the repo is accidentally published with an issue:

1. Set repository visibility to private immediately.
2. Rotate any exposed credentials if applicable.
3. Remove or rewrite the affected history.
4. Re-publish only after a clean scan.
