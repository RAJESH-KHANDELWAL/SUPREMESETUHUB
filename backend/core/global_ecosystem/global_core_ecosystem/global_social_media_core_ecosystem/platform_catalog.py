"""Canonical platform inventory, sourced from the Social Media API catalog."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

_DATA = Path(__file__).with_name("platform_catalog.json")
with _DATA.open("r", encoding="utf-8") as _stream:
    PLATFORM_DEFINITIONS: tuple[dict[str, Any], ...] = tuple(json.load(_stream))
_INDEX = {item["id"]: item for item in PLATFORM_DEFINITIONS}

def list_platforms() -> list[dict[str, Any]]:
    return [dict(item) for item in PLATFORM_DEFINITIONS]

def get_platform(platform_id: str) -> dict[str, Any]:
    key = platform_id.strip().lower().replace("-", "_")
    try:
        return dict(_INDEX[key])
    except KeyError as exc:
        raise LookupError(f"SOCIAL_MEDIA_PLATFORM_NOT_REGISTERED: {platform_id}") from exc

def platform_summary() -> dict[str, Any]:
    return {
        "success": True,
        "platform_count": len(PLATFORM_DEFINITIONS),
        "provider_count": sum(item["package_type"] == "PLATFORM" for item in PLATFORM_DEFINITIONS),
        "family_count": sum(item["package_type"] == "PLATFORM_FAMILY" for item in PLATFORM_DEFINITIONS),
        "live_connections_verified": 0,
        "platforms": list_platforms(),
    }
