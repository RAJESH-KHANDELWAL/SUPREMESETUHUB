"""Anthropic provider-owned API ecosystem catalog.

Catalog metadata only; authentication and live API calls are handled by the
shared integration layer, never by this module.
"""
from __future__ import annotations

ANTHROPIC_API_ECOSYSTEM = {
    "provider_id": "anthropic",
    "name": "ANTHROPIC API ECOSYSTEM",
    "status": "CATALOG_AND_READINESS_ADAPTER",
    "live_connection_verified": False,
    "purpose": "Claude models and Anthropic developer APIs",
    "platforms_and_api_areas": [
        "Claude API", "Messages API", "Message Batches API", "Models API",
        "Token Counting API", "Files API", "Admin API and Workspaces",
        "Claude Managed Agents: Sessions and Environments",
        "Tool use, vision, streaming, prompt caching and extended thinking",
        "Workload Identity Federation",
    ],
    "related_ecosystems": ["AI", "DEVELOPER"],
    "credential_source": "environment_or_managed_secret_store",
    "children": [
        {"id": "messages", "name": "Messages API", "folder": "anthropic_messages_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "batches", "name": "Message Batches API", "folder": "anthropic_batches_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "models", "name": "Models API", "folder": "anthropic_models_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "token_counting", "name": "Token Counting API", "folder": "anthropic_token_counting_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "files", "name": "Files API", "folder": "anthropic_files_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "admin_workspaces", "name": "Admin API and Workspaces", "folder": "anthropic_admin_workspaces_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "managed_agents", "name": "Managed Agents, Sessions and Environments", "folder": "anthropic_managed_agents_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "tool_use", "name": "Tool Use and Agentic Capabilities", "folder": "anthropic_tool_use_api_ecosystem", "status": "CATALOG_SCAFFOLD"},
        {"id": "auth_identity", "name": "Authentication and Workload Identity Federation", "folder": "anthropic_auth_identity_ecosystem", "status": "CATALOG_SCAFFOLD"},
    ],
}


def list_anthropic_api_ecosystems() -> list[dict[str, str]]:
    """Return child catalog entries; this does not verify provider connectivity."""
    return [dict(item) for item in ANTHROPIC_API_ECOSYSTEM["children"]]


__all__ = ["ANTHROPIC_API_ECOSYSTEM", "list_anthropic_api_ecosystems"]
