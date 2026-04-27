#!/usr/bin/env python3
"""Small public-readiness scan for this case-study package.

This is not a replacement for a full secret scanner. It catches the patterns that
should never appear in this public-facing draft package.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = {
    "local_absolute_path": re.compile(r"/Users/[A-Za-z0-9_.-]+"),
    "discord_snowflake": re.compile(r"\b1[0-9]{16,20}\b"),
    "private_email_example": re.compile(r"ulttla@gmail\.com", re.I),
    "openclaw_config": re.compile(r"openclaw\.json", re.I),
    "runtime_port_example": re.compile(r"\b18789\b"),
    "hosting_service_id_shape": re.compile(r"af[0-9a-f]{14,}", re.I),
}
ALLOW_WORDS = {
    "secret", "secrets", "token", "tokens", "password", "passwords", ".env"
}
TEXT_SUFFIXES = {".md", ".txt", ".json", ".py", ".gitignore"}

failures: list[str] = []
for path in ROOT.rglob("*"):
    if ".git" in path.parts or not path.is_file():
        continue
    if path.name == "validate_public_package.py" or path.suffix not in TEXT_SUFFIXES:
        continue
    text = path.read_text(errors="ignore")
    for name, pattern in FORBIDDEN.items():
        for match in pattern.finditer(text):
            failures.append(f"{path.relative_to(ROOT)}: {name}: {match.group(0)}")

if failures:
    print("PUBLIC_PACKAGE_SCAN FAIL")
    for item in failures:
        print(item)
    raise SystemExit(1)

print("PUBLIC_PACKAGE_SCAN PASS")
