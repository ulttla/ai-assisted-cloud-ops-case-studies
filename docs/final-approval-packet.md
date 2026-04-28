# Final Approval Packet

This packet is the go/no-go checklist for publishing the AI-assisted cloud ops portfolio package.

## Current draft artifacts

### GitHub case-study package

- Repository name proposal: `gun-openclaw-use-cases`
- Local state: clean public-facing draft commit
- Current visibility: local only
- Public release action pending approval: create public GitHub repository and push

### gunkr.com portfolio draft

- Local state: one commit ahead of the existing gunkr.com remote
- New section: `AI Engineering Lab`
- New pages:
  - `projects/azvision-network-path-analysis.html`
  - `projects/ai-assisted-engineering-control-plane.html`
  - `projects/long-work-window-playbook.html`
- Public release action pending approval: push/deploy or hosting File Manager update

## Evidence before approval

- Public package scan: PASS
- gunkr local link check: PASS
- gunkr new page sensitive-string scan: PASS
- Reviewer verdict: pass-with-fixes, no blocking issue
- Fixes applied: removed draft wording, added AzVision proof count, added existing-claim review note

## Approval options

### Option 1 — Draft only

Keep everything local. No external publication.

Recommended if existing employer/security/budget claims need more review first.

### Option 2 — Publish GitHub package only

Create and push the sanitized GitHub case-study repository first. Leave gunkr.com live site unchanged.

Recommended if you want a reviewable public artifact before changing the portfolio site.

### Option 3 — Publish GitHub package + gunkr.com portfolio update

Publish both the case-study repo and the portfolio pages.

Recommended only after final content review and link checks.

## Commands after approval

### GitHub package

```bash
cd /path/to/gun-openclaw-use-cases
scripts/validate_public_package.py
gh repo create ulttla/gun-openclaw-use-cases --public --source=. --remote=origin --push
```

### gunkr.com Git path

```bash
cd /path/to/gunkr.com
git status --short
git push origin main
```

Then verify hosting deploy status and live links.

## Rollback plan

### GitHub package

- If the repository was created but should not remain public, set it private immediately or delete it from GitHub after confirming no secrets were exposed.
- If a sensitive value was exposed, rotate that credential before re-publishing.

### gunkr.com

- Revert the local gunkr.com commit.
- Push the revert or restore previous files through hosting File Manager.
- Purge CDN if stale pages remain.

## Final human approval needed for

- creating public GitHub repo
- pushing any public repo
- pushing gunkr.com changes
- editing hosting File Manager
- purging CDN
