"""Canonical DeepSeek provider and capability catalog; metadata only."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

_CATALOG: dict[str, Any] = {
    "provider": "deepseek",
    "ecosystem_id": "DEEPSEEK-CORE-ECOSYSTEM",
    "name": "DEEPSEEK CORE ECOSYSTEM",
    "layer": "CORE",
    "status": "INTERFACE_ONLY",
    "live_provider_calls_enabled": False,
    "api_ecosystem_ref": "backend/api/global_ecosystem/global_api_ecosystem/deepseek_api_ecosystem",
    "capabilities": {
        "chat_completions": {
            "package": "deepseek_chat_completions_core_ecosystem",
            "endpoint": "POST /chat/completions",
            "status": "CONTRACT_ONLY",
            "live_enabled": False,
        },
        "responses": {
            "package": "deepseek_responses_core_ecosystem",
            "endpoint": "POST /responses",
            "status": "CONTRACT_ONLY",
            "live_enabled": False,
        },
        "search": {
            "package": "deepseek_search_core_ecosystem",
            "endpoint": "POST /v1/tools/search",
            "status": "CONTRACT_ONLY",
            "live_enabled": False,
        },
        "fetch": {
            "package": "deepseek_fetch_core_ecosystem",
            "endpoint": "POST /v1/tools/fetch",
            "status": "CONTRACT_ONLY",
            "live_enabled": False,
        },
    },
}


def get_catalog() -> dict[str, Any]:
    """Return a defensive copy of provider metadata."""
    return deepcopy(_CATALOG)


def list_capabilities() -> dict[str, dict[str, Any]]:
    """Return registered capability metadata."""
    return deepcopy(_CATALOG["capabilities"])
