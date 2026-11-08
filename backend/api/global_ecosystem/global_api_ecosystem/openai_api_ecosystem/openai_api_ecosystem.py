"""Canonical OpenAI provider product/service catalog.

This registry mirrors the provider-owned product hierarchy: named OpenAI
products and developer platforms are child ecosystems under OPENAI API ECOSYSTEM.
It is catalog metadata, not a claim that each product exposes a public API.
"""
from __future__ import annotations

PROVIDER_ID = "openai"
PROVIDER_NAME = "OPENAI API ECOSYSTEM"
PROVIDER_FOLDER = "backend/api/global_ecosystem/global_api_ecosystem/openai_api_ecosystem"

OPENAI_API_CAPABILITIES = [
    'platform',
    'models',
    'responses',
    'chat_completions',
    'embeddings',
    'images',
    'audio',
    'realtime',
    'files',
    'batch',
    'vector_stores',
    'fine_tuning',
    'moderation',
    'evaluations',
    'webhooks',
    'developer_tools',
    'assistants_migration'
]

OPENAI_PRODUCTS = (
    {"id": "chatgpt", "name": "OPENAI CHATGPT API ECOSYSTEM", "folder": "openai_chatgpt_api_ecosystem", "status": "active_catalog", "description": "OpenAI's main conversational product. Product features such as chat, search, voice, file analysis, projects, custom GPTs and deep research belong here unless OpenAI exposes them as a distinct platform/API."},
    {"id": "chatgpt_business", "name": "OPENAI CHATGPT BUSINESS API ECOSYSTEM", "folder": "openai_chatgpt_business_api_ecosystem", "status": "active_catalog", "description": "Business workspace edition with organization collaboration and administrative controls. Treat as a ChatGPT plan/workspace offering, not a separate model API."},
    {"id": "chatgpt_enterprise", "name": "OPENAI CHATGPT ENTERPRISE API ECOSYSTEM", "folder": "openai_chatgpt_enterprise_api_ecosystem", "status": "active_catalog", "description": "Enterprise workspace offering with organization-level administration, security and deployment controls. Availability and features depend on contract and workspace settings."},
    {"id": "chatgpt_education", "name": "OPENAI CHATGPT EDU API ECOSYSTEM", "folder": "openai_chatgpt_education_api_ecosystem", "status": "active_catalog", "description": "Education-focused ChatGPT offering for eligible institutions. Access and controls depend on institutional deployment."},
    {"id": "chatgpt_health", "name": "OPENAI CHATGPT HEALTH API ECOSYSTEM", "folder": "openai_chatgpt_health_api_ecosystem", "status": "availability_dependent_catalog", "description": "Health-focused ChatGPT experience. This is a product surface, not a medical diagnosis API; availability and connected-data eligibility must be checked."},
    {"id": "codex", "name": "OPENAI CODEX API ECOSYSTEM", "folder": "openai_codex_api_ecosystem", "status": "active_catalog", "description": "OpenAI's coding agent across supported app, CLI, IDE and cloud workflows. Codex SDK and app-server integration details are documented separately within this child."},
    {"id": "dots", "name": "OPENAI DOTS API ECOSYSTEM", "folder": "openai_dots_api_ecosystem", "status": "availability_dependent_catalog", "description": "OpenAI personal agent product for ongoing work. Treat setup, access, integrations and availability as product-specific and verify current official documentation."},
    {"id": "agents_api", "name": "OPENAI AGENTS API API ECOSYSTEM", "folder": "openai_agents_api_ecosystem", "status": "public_beta_catalog", "description": "Managed agent runtime/API using OpenAI's Codex harness, durable sessions, orchestration and supported execution environments."},
    {"id": "agents_sdk", "name": "OPENAI AGENTS SDK API ECOSYSTEM", "folder": "openai_agents_sdk_api_ecosystem", "status": "active_catalog", "description": "Developer SDK for building agent loops, tools, handoffs and application-managed agent workflows."},
    {"id": "apps_sdk", "name": "OPENAI APPS SDK API ECOSYSTEM", "folder": "openai_apps_sdk_api_ecosystem", "status": "active_catalog", "description": "Developer toolkit for building apps and experiences that run within ChatGPT, including supported MCP-based integrations."},
    {"id": "chatkit", "name": "OPENAI CHATKIT API ECOSYSTEM", "folder": "openai_chatkit_api_ecosystem", "status": "active_catalog", "description": "Developer toolkit for embedding a chat experience into an application, using supported OpenAI platform components."},
    {"id": "sdk_libraries", "name": "OPENAI OPENAI SDKS API ECOSYSTEM", "folder": "openai_sdk_libraries_api_ecosystem", "status": "active_catalog", "description": "Official API client libraries and developer SDKs for supported languages. Keep language-specific client libraries cataloged under this service."},
    {"id": "plugins_mcp", "name": "OPENAI PLUGINS AND MCP API ECOSYSTEM", "folder": "openai_plugins_mcp_api_ecosystem", "status": "active_catalog", "description": "Extension and tool integration ecosystem spanning supported ChatGPT/Codex plugin surfaces and Model Context Protocol servers. Distinguish product plugins from MCP protocol integrations."},
    {"id": "sora", "name": "OPENAI SORA (RETIRED REFERENCE) API ECOSYSTEM", "folder": "openai_sora_api_ecosystem", "status": "retired_reference_only", "description": "Historical product reference only. OpenAI's Sora web/app experience and Sora API were discontinued in 2026; do not expose this as an active integration."},
)

OPENAI_API_ECOSYSTEM = {
    "provider_id": PROVIDER_ID,
    "name": PROVIDER_NAME,
    "folder": PROVIDER_FOLDER,
    "status": "PRODUCT_AND_SERVICE_CATALOG",
    "live_connection_verified": False,
    "platforms": [
        "ChatGPT", "Codex", "Dots", "OpenAI API Platform",
        "Agents API", "Agents SDK", "Apps SDK", "ChatKit", "OpenAI SDKs",
    ],
    "product_count": len(OPENAI_PRODUCTS),
    "children": [dict(item) for item in OPENAI_PRODUCTS],
    "api_capabilities": list(OPENAI_API_CAPABILITIES),
    "related_ecosystems": ["AI", "DEVELOPER", "TOOLS", "LANGUAGE", "DATABASE", "PLATFORMS"],
    "security_requirements": [
        "authenticated_user_scope",
        "tenant_scoped_authorization",
        "encrypted_credentials_at_rest",
        "never_log_or_return_api_keys",
        "redact_authorization_headers",
        "rate_limits_and_request_timeouts",
        "usage_metering_and_cost_controls",
        "credential_rotation_and_revoke",
    ],
}


def list_openai_api_ecosystems() -> dict[str, object]:
    """Return the OpenAI product/service catalog; no live connection is made."""
    children = [dict(item) for item in OPENAI_PRODUCTS]
    return {
        "success": True,
        "provider_id": PROVIDER_ID,
        "provider": PROVIDER_NAME,
        "status": OPENAI_API_ECOSYSTEM["status"],
        "live_connection_verified": False,
        "count": len(children),
        "ecosystems": children,
    }


def list_openai_api_capabilities() -> dict[str, object]:
    """Return API capability families separately from named OpenAI products."""
    return {
        "success": True,
        "count": len(OPENAI_API_CAPABILITIES),
        "capabilities": list(OPENAI_API_CAPABILITIES),
    }
