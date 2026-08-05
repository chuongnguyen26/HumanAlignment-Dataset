#!/usr/bin/env python3
"""Print QualAlign domain sizes and column schemas."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qualalign.load import DOMAINS, load_domain, load_research_questions  # noqa: E402


def main() -> None:
    print(f"{'domain':<24} {'chunks':>7}  columns")
    print("-" * 72)
    total = 0
    for domain in DOMAINS:
        df = load_domain(domain)
        total += len(df)
        cols = ", ".join(df.columns)
        print(f"{domain:<24} {len(df):>7}  {cols}")
    print("-" * 72)
    print(f"{'TOTAL':<24} {total:>7}")
    print()
    for domain in DOMAINS:
        print(f"### {domain}")
        print(load_research_questions(domain).rstrip())
        print()


if __name__ == "__main__":
    main()
