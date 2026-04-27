#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
./scripts/validate_public_package.py
git diff --check
git status --short
printf '\nPre-publish check completed. Review output above before pushing.\n'
