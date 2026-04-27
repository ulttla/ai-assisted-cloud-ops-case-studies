# Visual QA Notes

## What to inspect before live publish

### Desktop

- The `AI-Assisted Cloud Ops` section should appear before the existing `Key Projects` section.
- The three new cards should be easy to scan in this order:
  1. AzVision Network Path Analysis
  2. AI-Assisted Engineering Control Plane
  3. Long Work Window Playbook
- Card copy should feel outcome-oriented, not tool-list oriented.
- Case-study pages should have visible `Back to portfolio` links.

### Mobile

- Cards should stack cleanly.
- CTA buttons should remain full-width and tappable.
- Long page headings should wrap without horizontal overflow.
- The badge row should not create horizontal scroll.

### Links

Clean URLs expected after deploy:

- `/projects/azvision-network-path-analysis`
- `/projects/ai-assisted-engineering-control-plane`
- `/projects/long-work-window-playbook`

`.html` URLs should either work or redirect cleanly according to the deployed `.htaccess` behavior.

## Current local checks

- Local HTTP check: PASS
- Static link check: PASS
- Sensitive string check: PASS
- Live pre-deploy baseline: root is live; new pages are not yet deployed

## Suggested screenshot set

If screenshots are added later, use only sanitized screenshots:

- Portfolio homepage with AI-assisted cards visible
- AzVision case-study page hero + proof card
- Optional synthetic evidence UI, not real Azure data
