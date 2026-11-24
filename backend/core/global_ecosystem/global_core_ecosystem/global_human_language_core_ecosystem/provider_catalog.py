"""Canonical provider registry loaded from provider_catalog.json."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from typing import Any

_DATA_PATH = Path(__file__).with_name("provider_catalog.json")
_DATA = json.loads(_DATA_PATH.read_text(encoding="utf-8"))
HUMAN_LANGUAGE_PROVIDERS = tuple(_DATA["providers"])


def get_provider_catalog() -> list[dict[str, Any]]:
    return deepcopy(list(HUMAN_LANGUAGE_PROVIDERS))


def get_provider(provider_id: str) -> dict[str, Any] | None:
    needle = provider_id.strip().casefold()
    for item in HUMAN_LANGUAGE_PROVIDERS:
        if item["provider_id"].casefold() == needle or item["provider_key"].casefold() == needle:
            return deepcopy(item)
    return None


def provider_catalog_summary() -> dict[str, Any]:
    return {
        "provider_count": len(HUMAN_LANGUAGE_PROVIDERS),
        "live_connections_verified": 0,
        "provider_coverage_exhaustive": bool(_DATA.get("provider_coverage_exhaustive", False)),
    }
