"""Canonical Anthropic Core catalog; inventory metadata, not API implementation."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

ANTHROPIC_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "ANTHROPIC-CORE-ECOSYSTEM",
    "name": "ANTHROPIC CORE ECOSYSTEM",
    "provider": "anthropic",
    "ecosystem_type": "PROVIDER_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "REGISTERED",
    "enabled": True,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem",
    "existing_anthropic_core_ref": "backend/global_ecosystem/anthropic_ecosystem",
    "capabilities": [
        "ANTHROPIC_PROVIDER_CORE_REGISTRY",
        "ANTHROPIC_PRODUCT_DISCOVERY",
        "TENANT_SCOPED_CONTEXT",
        "OPAQUE_SECRET_REFERENCE",
        "CAPABILITY_POLICY_METADATA",
        "LIFECYCLE_AND_READINESS"
    ],
    "children": [
        {
            "ecosystem_id": "ANTHROPIC-MESSAGES-CORE-ECOSYSTEM",
            "name": "ANTHROPIC MESSAGES CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "ANTHROPIC-CORE-ECOSYSTEM",
            "product_id": "messages",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_messages_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_messages_core_ecosystem",
            "capabilities": [
                "ANTHROPIC_MESSAGES_CREATE",
                "ANTHROPIC_MESSAGES_STREAM",
                "ANTHROPIC_MESSAGES_TOOL_USE"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": True,
            "connected": False,
            "live_connection_verified": False,
            "requires_explicit_permission": False
        },
        {
            "ecosystem_id": "ANTHROPIC-BATCHES-CORE-ECOSYSTEM",
            "name": "ANTHROPIC MESSAGE BATCHES CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "ANTHROPIC-CORE-ECOSYSTEM",
            "product_id": "batches",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_batches_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_batches_core_ecosystem",
            "capabilities": [
                "ANTHROPIC_BATCH_CREATE",
                "ANTHROPIC_BATCH_STATUS",
                "ANTHROPIC_BATCH_RESULTS"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": True,
            "connected": False,
            "live_connection_verified": False,
            "requires_explicit_permission": False
        },
        {
            "ecosystem_id": "ANTHROPIC-MODELS-CORE-ECOSYSTEM",
            "name": "ANTHROPIC MODELS CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "ANTHROPIC-CORE-ECOSYSTEM",
            "product_id": "models",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_models_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_models_core_ecosystem",
            "capabilities": [
                "ANTHROPIC_MODELS_LIST",
                "ANTHROPIC_MODEL_METADATA"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": True,
            "connected": False,
            "live_connection_verified": False,
            "requires_explicit_permission": False
        },
        {
            "ecosystem_id": "ANTHROPIC-TOKEN-COUNTING-CORE-ECOSYSTEM",
            "name": "ANTHROPIC TOKEN COUNTING CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "ANTHROPIC-CORE-ECOSYSTEM",
            "product_id": "token_counting",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_token_counting_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_token_counting_core_ecosystem",
            "capabilities": [
                "ANTHROPIC_TOKEN_COUNT_ESTIMATE"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": True,
            "connected": False,
            "live_connection_verified": False,
            "requires_explicit_permission": False
        },
        {
            "ecosystem_id": "ANTHROPIC-FILES-CORE-ECOSYSTEM",
            "name": "ANTHROPIC FILES CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "ANTHROPIC-CORE-ECOSYSTEM",
            "product_id": "files",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_files_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_files_core_ecosystem",
            "capabilities": [
                "ANTHROPIC_FILES_LIST",
                "ANTHROPIC_FILES_UPLOAD",
                "ANTHROPIC_FILES_RETRIEVE",
                "ANTHROPIC_FILES_DELETE"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": True,
            "connected": False,
            "live_connection_verified": False,
            "requires_explicit_permission": True
        },
        {
            "ecosystem_id": "ANTHROPIC-ADMIN-WORKSPACES-CORE-ECOSYSTEM",
            "name": "ANTHROPIC ADMIN WORKSPACES CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "ANTHROPIC-CORE-ECOSYSTEM",
            "product_id": "admin_workspaces",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_admin_workspaces_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_admin_workspaces_core_ecosystem",
            "capabilities": [
                "ANTHROPIC_WORKSPACE_LIST",
                "ANTHROPIC_WORKSPACE_ADMIN"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": True,
            "connected": False,
            "live_connection_verified": False,
            "requires_explicit_permission": True
        },
        {
            "ecosystem_id": "ANTHROPIC-MANAGED-AGENTS-CORE-ECOSYSTEM",
            "name": "ANTHROPIC MANAGED AGENTS CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "ANTHROPIC-CORE-ECOSYSTEM",
            "product_id": "managed_agents",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_managed_agents_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_managed_agents_core_ecosystem",
            "capabilities": [
                "ANTHROPIC_MANAGED_AGENT_SESSIONS",
                "ANTHROPIC_MANAGED_AGENT_ENVIRONMENTS"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": True,
            "connected": False,
            "live_connection_verified": False,
            "requires_explicit_permission": True
        },
        {
            "ecosystem_id": "ANTHROPIC-TOOL-USE-CORE-ECOSYSTEM",
            "name": "ANTHROPIC TOOL USE CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "ANTHROPIC-CORE-ECOSYSTEM",
            "product_id": "tool_use",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_tool_use_api_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_tool_use_core_ecosystem",
            "capabilities": [
                "ANTHROPIC_TOOL_DEFINITION",
                "ANTHROPIC_TOOL_CHOICE",
                "ANTHROPIC_TOOL_HANDOFF"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": True,
            "connected": False,
            "live_connection_verified": False,
            "requires_explicit_permission": False
        },
        {
            "ecosystem_id": "ANTHROPIC-AUTH-IDENTITY-CORE-ECOSYSTEM",
            "name": "ANTHROPIC AUTHENTICATION AND IDENTITY CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_SERVICE",
            "parent_id": "ANTHROPIC-CORE-ECOSYSTEM",
            "product_id": "auth_identity",
            "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_auth_identity_ecosystem",
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_auth_identity_core_ecosystem",
            "capabilities": [
                "ANTHROPIC_CREDENTIAL_READINESS",
                "ANTHROPIC_WORKLOAD_IDENTITY_BOUNDARY",
                "ANTHROPIC_CREDENTIAL_ROTATION_BOUNDARY"
            ],
            "status": "CORE_CATALOG_ONLY",
            "enabled": True,
            "connected": False,
            "live_connection_verified": False,
            "requires_explicit_permission": True
        }
    ]
}

def get_anthropic_core_catalog() -> dict[str, Any]:
    return deepcopy(ANTHROPIC_CORE_ECOSYSTEM)

def list_anthropic_core_modules() -> list[dict[str, Any]]:
    return deepcopy(ANTHROPIC_CORE_ECOSYSTEM["children"])
