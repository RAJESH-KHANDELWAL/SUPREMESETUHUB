"""Helpers for the Global Professional Work Core Ecosystem."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
DOMAINS_FILE = ROOT / "professional_work_domains.json"


def load_domains() -> dict[str, Any]:
    """Load the professional-work domain taxonomy."""
    with DOMAINS_FILE.open("r", encoding="utf-8") as stream:
        payload = json.load(stream)
    if payload.get("ecosystem") != "global_professional_work_core_ecosystem":
        raise ValueError("Unexpected ecosystem identifier")
    return payload


def list_domains() -> list[dict[str, Any]]:
    """Return the configured professional-work domains."""
    return load_domains().get("domains", [])


def validate_domain_record(record: dict[str, Any]) -> bool:
    """Check the minimum shape required for a professional domain record."""
    return (
        isinstance(record, dict)
        and isinstance(record.get("id"), str)
        and bool(record["id"].strip())
        and isinstance(record.get("name"), str)
        and bool(record["name"].strip())
    )
