"""Canonical OpenAI Core provider and product-family catalog.

This module is a Core-owned metadata registry. It intentionally does not import
OpenAI API modules, SDK clients, credentials, or runtime executors.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

PROVIDER_ID = "openai"
PROVIDER_NAME = "OPENAI"
ECOSYSTEM_ID = "OPENAI-CORE-ECOSYSTEM"
API_CATALOG_REF = "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_api_ecosystem.py"
CORE_ROOT = "backend/core/global_ecosystem/global_core_ecosystem/openai_core_ecosystem/"

PRODUCTS: tuple[dict[str, Any], ...] = (
    {
        "id": "chatgpt",
        "ecosystem_id": "OPENAI-CHATGPT-CORE-ECOSYSTEM",
        "name": "OPENAI CHATGPT CORE ECOSYSTEM",
        "display_name": "ChatGPT",
        "provider_id": PROVIDER_ID,
        "status": "active_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_chatgpt_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_chatgpt_api_ecosystem",
        "capabilities": ["CHATGPT_PRODUCT_DISCOVERY","CHATGPT_FEATURE_METADATA","CHATGPT_WORKSPACE_FEATURE_BOUNDARY"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "chatgpt_business",
        "ecosystem_id": "OPENAI-CHATGPT-BUSINESS-CORE-ECOSYSTEM",
        "name": "OPENAI CHATGPT BUSINESS CORE ECOSYSTEM",
        "display_name": "ChatGPT Business",
        "provider_id": PROVIDER_ID,
        "status": "active_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_chatgpt_business_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_chatgpt_business_api_ecosystem",
        "capabilities": ["BUSINESS_WORKSPACE_METADATA","ORGANIZATION_ADMINISTRATION_BOUNDARY","BUSINESS_PLAN_ENTITLEMENT_METADATA"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "chatgpt_enterprise",
        "ecosystem_id": "OPENAI-CHATGPT-ENTERPRISE-CORE-ECOSYSTEM",
        "name": "OPENAI CHATGPT ENTERPRISE CORE ECOSYSTEM",
        "display_name": "ChatGPT Enterprise",
        "provider_id": PROVIDER_ID,
        "status": "active_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_chatgpt_enterprise_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_chatgpt_enterprise_api_ecosystem",
        "capabilities": ["ENTERPRISE_WORKSPACE_METADATA","ENTERPRISE_SECURITY_BOUNDARY","CONTRACT_AND_ENTITLEMENT_METADATA"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "chatgpt_education",
        "ecosystem_id": "OPENAI-CHATGPT-EDUCATION-CORE-ECOSYSTEM",
        "name": "OPENAI CHATGPT EDUCATION CORE ECOSYSTEM",
        "display_name": "ChatGPT Education",
        "provider_id": PROVIDER_ID,
        "status": "active_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_chatgpt_education_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_chatgpt_education_api_ecosystem",
        "capabilities": ["EDUCATION_WORKSPACE_METADATA","INSTITUTIONAL_ACCESS_BOUNDARY","EDUCATION_ENTITLEMENT_METADATA"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "chatgpt_health",
        "ecosystem_id": "OPENAI-CHATGPT-HEALTH-CORE-ECOSYSTEM",
        "name": "OPENAI CHATGPT HEALTH CORE ECOSYSTEM",
        "display_name": "ChatGPT Health",
        "provider_id": PROVIDER_ID,
        "status": "availability_dependent_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_chatgpt_health_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_chatgpt_health_api_ecosystem",
        "capabilities": ["HEALTH_PRODUCT_METADATA","CONNECTED_HEALTH_DATA_ELIGIBILITY_BOUNDARY","NOT_A_MEDICAL_DIAGNOSIS_API"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "codex",
        "ecosystem_id": "OPENAI-CODEX-CORE-ECOSYSTEM",
        "name": "OPENAI CODEX CORE ECOSYSTEM",
        "display_name": "Codex",
        "provider_id": PROVIDER_ID,
        "status": "active_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_codex_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_codex_api_ecosystem",
        "capabilities": ["CODING_AGENT_PRODUCT_METADATA","CODEX_APP_CLI_IDE_METADATA","DEVELOPER_WORKFLOW_DISCOVERY"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "dots",
        "ecosystem_id": "OPENAI-DOTS-CORE-ECOSYSTEM",
        "name": "OPENAI DOTS CORE ECOSYSTEM",
        "display_name": "Dots",
        "provider_id": PROVIDER_ID,
        "status": "availability_dependent_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_dots_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_dots_api_ecosystem",
        "capabilities": ["PERSONAL_AGENT_PRODUCT_METADATA","CONNECTED_APP_AVAILABILITY_METADATA","ACCOUNT_ELIGIBILITY_BOUNDARY"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "agents_api",
        "ecosystem_id": "OPENAI-AGENTS-API-CORE-ECOSYSTEM",
        "name": "OPENAI AGENTS API CORE ECOSYSTEM",
        "display_name": "Agents API",
        "provider_id": PROVIDER_ID,
        "status": "public_beta_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_agents_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_agents_api_ecosystem",
        "capabilities": ["MANAGED_AGENT_API_METADATA","AGENT_RUNTIME_DISCOVERY","PUBLIC_BETA_AVAILABILITY_BOUNDARY"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "agents_sdk",
        "ecosystem_id": "OPENAI-AGENTS-SDK-CORE-ECOSYSTEM",
        "name": "OPENAI AGENTS SDK CORE ECOSYSTEM",
        "display_name": "Agents SDK",
        "provider_id": PROVIDER_ID,
        "status": "active_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_agents_sdk_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_agents_sdk_api_ecosystem",
        "capabilities": ["AGENT_SDK_METADATA","TOOL_HANDOFF_METADATA","APPLICATION_MANAGED_AGENT_WORKFLOWS"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "apps_sdk",
        "ecosystem_id": "OPENAI-APPS-SDK-CORE-ECOSYSTEM",
        "name": "OPENAI APPS SDK CORE ECOSYSTEM",
        "display_name": "Apps SDK",
        "provider_id": PROVIDER_ID,
        "status": "active_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_apps_sdk_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_apps_sdk_api_ecosystem",
        "capabilities": ["CHATGPT_APP_DEVELOPMENT_METADATA","MCP_APP_INTEGRATION_METADATA","APP_REVIEW_AND_ELIGIBILITY_BOUNDARY"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "chatkit",
        "ecosystem_id": "OPENAI-CHATKIT-CORE-ECOSYSTEM",
        "name": "OPENAI CHATKIT CORE ECOSYSTEM",
        "display_name": "ChatKit",
        "provider_id": PROVIDER_ID,
        "status": "active_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_chatkit_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_chatkit_api_ecosystem",
        "capabilities": ["EMBEDDED_CHAT_EXPERIENCE_METADATA","CHAT_UI_INTEGRATION_METADATA","APPLICATION_HOSTED_EXPERIENCE_BOUNDARY"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "sdk_libraries",
        "ecosystem_id": "OPENAI-SDK-LIBRARIES-CORE-ECOSYSTEM",
        "name": "OPENAI OPENAI SDK LIBRARIES CORE ECOSYSTEM",
        "display_name": "OpenAI SDK Libraries",
        "provider_id": PROVIDER_ID,
        "status": "active_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_sdk_libraries_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_sdk_libraries_api_ecosystem",
        "capabilities": ["OFFICIAL_CLIENT_SDK_CATALOG","LANGUAGE_CLIENT_METADATA","SDK_VERSION_COMPATIBILITY_BOUNDARY"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "plugins_mcp",
        "ecosystem_id": "OPENAI-PLUGINS-MCP-CORE-ECOSYSTEM",
        "name": "OPENAI PLUGINS AND MCP CORE ECOSYSTEM",
        "display_name": "Plugins and MCP",
        "provider_id": PROVIDER_ID,
        "status": "active_catalog",
        "enabled": True,
        "core_module": CORE_ROOT + "openai_plugins_mcp_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_plugins_mcp_api_ecosystem",
        "capabilities": ["EXTENSION_DISCOVERY_METADATA","MCP_SERVER_METADATA","PLUGIN_AND_PROTOCOL_DISTINCTION"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
    {
        "id": "sora",
        "ecosystem_id": "OPENAI-SORA-CORE-ECOSYSTEM",
        "name": "OPENAI SORA (RETIRED REFERENCE) CORE ECOSYSTEM",
        "display_name": "Sora (retired reference)",
        "provider_id": PROVIDER_ID,
        "status": "retired_reference_only",
        "enabled": False,
        "core_module": CORE_ROOT + "openai_sora_core_ecosystem",
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem/openai_sora_api_ecosystem",
        "capabilities": ["RETIRED_PRODUCT_REFERENCE_ONLY","HISTORICAL_PRODUCT_METADATA","NOT_AVAILABLE_FOR_NEW_CONNECTIONS"],
        "connected": False,
        "live_connection_verified": False,
        "api_transport_in_core": False,
        "engine_execution_in_core": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
    },
)

OPENAI_API_CAPABILITIES: tuple[str, ...] = ["platform","models","responses","chat_completions","embeddings","images","audio","realtime","files","batch","vector_stores","fine_tuning","moderation","evaluations","webhooks","developer_tools","assistants_migration"]

OPENAI_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": ECOSYSTEM_ID,
    "name": "OPENAI CORE ECOSYSTEM",
    "provider": PROVIDER_ID,
    "provider_name": PROVIDER_NAME,
    "ecosystem_type": "PROVIDER_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "CORE_CATALOG_ONLY",
    "enabled": True,
    "core_module": CORE_ROOT,
    "api_catalog_ref": API_CATALOG_REF,
    "capabilities": [
        "OPENAI_PROVIDER_IDENTITY",
        "OPENAI_PRODUCT_DISCOVERY",
        "OPENAI_DOMAIN_TAXONOMY",
        "OPENAI_API_CAPABILITY_METADATA",
        "TENANT_SCOPED_POLICY_BOUNDARY",
        "SECRET_REFERENCE_BOUNDARY",
        "PRODUCT_LIFECYCLE_AND_READINESS",
        "DEPENDENCY_DISCOVERY",
    ],
    "children": [dict(item) for item in PRODUCTS],
    "product_count": len(PRODUCTS),
    "api_capability_count": len(OPENAI_API_CAPABILITIES),
    "live_connection_verified": False,
    "api_calls_performed": 0,
    "api_transport_in_core": False,
    "engine_execution_in_core": False,
    "master_catalog": {
        "path": "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
        "access_mode": "READ_ONLY_ON_DEMAND",
        "target_unique_entries": 2468,
        "current_unique_entries_at_source_snapshot": 246,
        "canonical_entry_ids": [
            "S09_artificial_intelligence",
            "S09_machine_learning",
            "S09_software",
            "S09_cloud_computing",
            "S09_data_analytics",
            "S09_cybersecurity",
        ],
        "catalog_entries_added": 0,
        "policy": "Do not manufacture entries to reach the target.",
    },
}


def get_openai_core_catalog() -> dict[str, Any]:
    """Return a defensive copy of the provider catalog."""
    return deepcopy(OPENAI_CORE_ECOSYSTEM)


def list_openai_core_modules() -> tuple[dict[str, Any], ...]:
    """Return defensive copies of all 14 registered product/service families."""
    return tuple(deepcopy(item) for item in PRODUCTS)


def get_openai_core_module(product_id: str) -> dict[str, Any] | None:
    """Find a product by service ID, ecosystem ID, or display name."""
    needle = str(product_id).strip().casefold()
    if not needle:
        return None
    for item in PRODUCTS:
        if needle in {
            item["id"].casefold(),
            item["ecosystem_id"].casefold(),
            item["display_name"].casefold(),
            item["name"].casefold(),
        }:
            return deepcopy(item)
    return None


def validate_openai_core_catalog() -> tuple[str, ...]:
    """Return catalog consistency errors without external API calls."""
    errors: list[str] = []
    seen: set[str] = set()
    for item in PRODUCTS:
        product_id = item.get("id")
        if not isinstance(product_id, str) or not product_id.strip():
            errors.append("PRODUCT_ID_REQUIRED")
            continue
        if product_id in seen:
            errors.append(f"DUPLICATE_PRODUCT_ID:{product_id}")
        seen.add(product_id)
        for field in ("ecosystem_id", "name", "core_module", "api_catalog_ref"):
            if not item.get(field):
                errors.append(f"{product_id}:MISSING_{field.upper()}")
        if item.get("live_connection_verified") is not False:
            errors.append(f"{product_id}:UNVERIFIED_LIVE_CONNECTION_MUST_BE_FALSE")
        if item.get("api_transport_in_core") is not False:
            errors.append(f"{product_id}:API_TRANSPORT_MUST_REMAIN_OUTSIDE_CORE")
    if len(PRODUCTS) != 14:
        errors.append(f"EXPECTED_14_PRODUCT_FAMILIES_GOT_{len(PRODUCTS)}")
    return tuple(errors)


__all__ = [
    "API_CATALOG_REF", "ECOSYSTEM_ID", "OPENAI_API_CAPABILITIES",
    "OPENAI_CORE_ECOSYSTEM", "PRODUCTS", "get_openai_core_catalog",
    "get_openai_core_module", "list_openai_core_modules",
    "validate_openai_core_catalog",
]
