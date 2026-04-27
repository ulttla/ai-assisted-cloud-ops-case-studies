# Public Release Checklist

Use this checklist before converting this draft package into a public GitHub repository or a live portfolio page.

## Content

- [ ] AzVision case study has a clear problem / solution / outcome structure.
- [ ] AI-assisted workflow claims are scoped and not exaggerated.
- [ ] Test/build numbers match the specific work slice.
- [ ] All diagrams are logical architecture diagrams, not private runtime diagrams.
- [ ] Screenshots are either synthetic or fully redacted.
- [ ] Existing employer/project claims and security incident wording are approved for public use or rewritten more generally.
  - See `docs/existing-portfolio-claim-review.md`.

## Security

- [ ] No real tenant, subscription, resource group, or resource identifiers.
- [ ] No credentials, tokens, passwords, private config, or control panel details.
- [ ] No local absolute paths or private workspace structure.
- [ ] No internal channel IDs, approval shortcuts, or automation schedules.
- [ ] No raw development journal metadata.

## GitHub

- [ ] Start from a clean history or verify history with a secret scan.
- [ ] `.gitignore` excludes env/config/secret/temp files.
- [ ] README states the repository is sanitized.
- [ ] License file is present if public reuse is intended.
- [ ] Repository visibility change has explicit approval.

## gunkr.com

- [ ] Local preview works.
- [ ] Project links resolve without requiring `.html` in visible links.
- [ ] Mobile layout is checked.
- [ ] Live deploy, hosting file manager edit, and CDN purge are explicitly approved.
