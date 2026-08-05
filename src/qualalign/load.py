"""Load QualAlign domain annotations."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA_ROOT = ROOT / "benchmark_dataset"

DOMAINS = (
    "adhd_reddit",
    "data_sharing",
    "mental_health",
    "patient_deterioration",
    "scrum_quality",
    "search_systems",
    "shuffle_music",
    "stroke_wearables",
)


def list_domains() -> list[str]:
    return list(DOMAINS)


def load_domain(domain: str) -> pd.DataFrame:
    """Load chunk-level annotations for a domain."""
    if domain not in DOMAINS:
        raise ValueError(f"Unknown domain {domain!r}. Choose from: {DOMAINS}")
    path = DATA_ROOT / domain / "train_data_w_gt.csv"
    return pd.read_csv(path)


def load_research_questions(domain: str) -> str:
    """Return research questions text for a domain."""
    if domain not in DOMAINS:
        raise ValueError(f"Unknown domain {domain!r}. Choose from: {DOMAINS}")
    path = DATA_ROOT / domain / "research_questions.txt"
    return path.read_text(encoding="utf-8")


def load_all() -> dict[str, pd.DataFrame]:
    """Load all domains as a name → DataFrame map."""
    return {domain: load_domain(domain) for domain in DOMAINS}
