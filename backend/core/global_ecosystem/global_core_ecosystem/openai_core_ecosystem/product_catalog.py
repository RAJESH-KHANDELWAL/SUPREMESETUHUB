"""Product and API capability inventory for OpenAI Core."""
from __future__ import annotations

from typing import Any

from .catalog import OPENAI_API_CAPABILITIES, list_openai_core_modules


def list_openai_offerings() -> list[dict[str, Any]]:
    """Return the 14 named product/service families, not API operation names."""
    return list_openai_core_modules()


def openai_offerings_summary() -> dict[str, Any]:
    items = list_openai_offerings()
    counts: dict[str, int] = {}
    for item in items:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    return {
        "success": True,
        "count": len(items),
        "status_counts": counts,
        "offerings": items,
        "live_connection_verified": False,
    }


def list_openai_api_capabilities() -> dict[str, Any]:
    """Return API capability families separately from named product packages."""
    return {
        "success": True,
        "count": len(OPENAI_API_CAPABILITIES),
        "capabilities": list(OPENAI_API_CAPABILITIES),
    }


__all__ = [
    "list_openai_offerings", "openai_offerings_summary",
    "list_openai_api_capabilities",
]
