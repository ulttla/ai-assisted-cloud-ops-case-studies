# gunkr.com Deploy Plan

This document captures the safe deploy sequence for the portfolio draft pages.

## Current state

- Draft pages are created locally.
- Local source and dist copies are aligned.
- No live deploy has been performed.
- Hosting session may be available, but live publish still requires explicit approval.

## Local validation before deploy

```bash
python3 -m http.server 8012
curl -I http://127.0.0.1:8012/index.html
```

Expected:

- `index.html` returns HTTP 200.
- AI Engineering Lab section is present.
- New case-study pages are reachable.

## Deploy options

### Option A — Git push and hosting deploy

Use if hosting Git deployment is behaving reliably.

1. Push the local gunkr.com commit.
2. Trigger hosting deploy.
3. Verify live links.
4. Purge CDN if stale content remains.

### Option B — Hosting File Manager direct edit

Use if hosting Git deploy reports success but public files do not update.

1. Open hosting File Manager.
2. Update `public_html/index.html` and new `public_html/projects/*.html` files.
3. Save and verify timestamps.
4. Purge CDN.
5. Run live link checks.

## Approval gate

Do not perform Git push, hosting deploy, File Manager write, or CDN purge until Gun approves the final public draft.
