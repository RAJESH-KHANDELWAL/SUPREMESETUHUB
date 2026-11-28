"""Helpers for the Global Professional Service Work Business Core Ecosystem."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
DOMAINS_FILE = ROOT / "service_work_business_domains.json"


def ecosystem_manifest() -> dict[str, Any]:
    """Return the service-work business ecosystem manifest."""
    with DOMAINS_FILE.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def list_service_domains() -> list[dict[str, Any]]:
    """Return configured professional service-business domains."""
    return ecosystem_manifest().get("domains", [])


def validate_service_record(record: dict[str, Any]) -> bool:
    """Validate the minimum required service-provider record fields."""
    return (
        isinstance(record, dict)
        and isinstance(record.get("name"), str)
        and bool(record["name"].strip())
        and isinstance(record.get("service_domain"), str)
        and bool(record["service_domain"].strip())
        and isinstance(record.get("provider_type"), str)
        and bool(record["provider_type"].strip())
    )
