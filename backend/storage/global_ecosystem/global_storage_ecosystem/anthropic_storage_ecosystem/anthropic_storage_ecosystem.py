"""Anthropic storage capability catalog; deliberately performs no network calls."""
from __future__ import annotations

ANTHROPIC_STORAGE_ECOSYSTEM = {
    "provider_id": "anthropic",
    "ecosystem_id": "ANTHROPIC-STORAGE-ECOSYSTEM",
    "implementation_state": "CATALOG_AND_CONTRACTS",
    "connection_state": "NOT_CONFIGURED",
    "external_connections_verified": False,
    "is_general_purpose_cloud_storage": False,
    "children": [
        {
            "id": "anthropic_files_storage",
            "name": "Anthropic Files Storage",
            "folder": "anthropic_files_storage_ecosystem",
            "scope": "workspace",
            "api_owner": "anthropic_api_ecosystem/anthropic_files_api_ecosystem",
            "capabilities": ["UPLOAD", "LIST", "RETRIEVE_METADATA", "REFERENCE_IN_MESSAGES", "DELETE", "OPTIONAL_EXPIRY"],
            "limitations": ["UPLOADED_CONTENT_NOT_DOWNLOADABLE", "NO_IN_PLACE_MODIFY_OR_RENAME", "WORKSPACE_SHARED_ACCESS"],
            "status": "DOCUMENTED_API_NOT_CONNECTED",
        },
        {
            "id": "anthropic_managed_agents_session_storage",
            "name": "Anthropic Managed Agents Session Storage",
            "folder": "anthropic_managed_agents_session_storage_ecosystem",
            "scope": "session_or_environment",
            "api_owner": "anthropic_api_ecosystem/anthropic_managed_agents_api_ecosystem",
            "capabilities": ["SESSION_FILE_RESOURCES", "SESSION_OUTPUT_ARTIFACTS", "SUPPORTED_OUTPUT_DOWNLOAD"],
            "limitations": ["MANAGED_AGENTS_ENTITLEMENT_REQUIRED", "SESSION_LIFECYCLE_AND_SCOPE_APPLY"],
            "status": "DOCUMENTED_API_NOT_CONNECTED",
        },
    ],
}


def list_anthropic_storage_ecosystems() -> list[dict]:
    """Return defensive copies of child capability metadata."""
    return [
        {**item, "capabilities": list(item["capabilities"]), "limitations": list(item["limitations"])}
        for item in ANTHROPIC_STORAGE_ECOSYSTEM["children"]
    ]


__all__ = ["ANTHROPIC_STORAGE_ECOSYSTEM", "list_anthropic_storage_ecosystems"]
