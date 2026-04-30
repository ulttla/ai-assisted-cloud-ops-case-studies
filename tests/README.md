# Validation Notes

This public case-study repository does not run the private application test suite. Public validation is documented as scoped evidence from the original work slice:

- targeted backend tests: 110 passed
- frontend build: passed
- earlier backend regression: 235 passed

Future public validation should use synthetic fixtures only.

## Planned public validation

- Synthetic Azure NSG and route-table fixtures for reproducible path-analysis examples.
- Link-check smoke for the public docs tree.
- Claim-scan automation through `scripts/validate_public_package.py` extensions.
- Public release evidence checks that confirm examples remain sanitized and scoped.
