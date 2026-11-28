"""Canonical DeepSeek provider-owned API ecosystem metadata.

Catalog metadata only. This module does not authenticate or make network requests.
"""
from __future__ import annotations

DEEPSEEK_API_ECOSYSTEM = {
    "provider_id": "deepseek",
    "name": "DEEPSEEK API ECOSYSTEM",
    "status": "CONFIGURATION_READINESS_SCAFFOLD",
    "live_connection_verified": False,
    "api_base_url": "https://api.deepseek.com",
    "authentication": "Bearer API key via server-side DEEPSEEK_API_KEY",
    "api_families": [
        "chat_completions", "responses", "search", "fetch",
    ],
    "children": [
        {"id": "chat_completions", "name": "DEEPSEEK CHAT COMPLETIONS API ECOSYSTEM", "folder": "deepseek_chat_completions_api_ecosystem", "status": "catalog_scaffold"},
        {"id": "responses", "name": "DEEPSEEK RESPONSES API ECOSYSTEM", "folder": "deepseek_responses_api_ecosystem", "status": "catalog_scaffold"},
        {"id": "search", "name": "DEEPSEEK SEARCH API ECOSYSTEM", "folder": "deepseek_search_api_ecosystem", "status": "catalog_scaffold"},
        {"id": "fetch", "name": "DEEPSEEK FETCH API ECOSYSTEM", "folder": "deepseek_fetch_api_ecosystem", "status": "catalog_scaffold"},
    ],
    "adapter_path": "backend/integrations/providers/deepseek.py",
    "credential_source": "server_side_secret_store",
}


def list_deepseek_api_ecosystems() -> dict[str, object]:
    """List DeepSeek API-family catalogs without claiming live connectivity."""
    children = [dict(item) for item in DEEPSEEK_API_ECOSYSTEM["children"]]
    return {
        "success": True,
        "provider": DEEPSEEK_API_ECOSYSTEM["name"],
        "status": DEEPSEEK_API_ECOSYSTEM["status"],
        "live_connection_verified": False,
        "count": len(children),
        "ecosystems": children,
    }


__all__ = ["DEEPSEEK_API_ECOSYSTEM", "list_deepseek_api_ecosystems"]
