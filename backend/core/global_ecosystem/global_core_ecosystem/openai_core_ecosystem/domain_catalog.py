"""OpenAI Core domains mapped to existing products and API capability families."""
from __future__ import annotations

from collections import Counter
from typing import Any

from .catalog import OPENAI_API_CAPABILITIES, list_openai_core_modules

DOMAIN_DEFINITIONS: dict[str, dict[str, Any]] = {
    "PROVIDER_GOVERNANCE": {
        "name": "Provider Governance",
        "purpose": "Provider identity, product registration, lifecycle, catalog integrity and provider-level readiness.",
        "product_ids": [],
        "api_capabilities": [],
    },
    "CHATGPT_AND_WORKSPACE": {
        "name": "ChatGPT and Workspace",
        "purpose": "ChatGPT product surfaces, workspace editions, institutional and health-product availability boundaries.",
        "product_ids": ["chatgpt","chatgpt_business","chatgpt_enterprise","chatgpt_education","chatgpt_health"],
        "api_capabilities": [],
    },
    "AGENT_RUNTIME_AND_ORCHESTRATION": {
        "name": "Agent Runtime and Orchestration",
        "purpose": "Managed Agents API, Agents SDK and personal-agent product discovery.",
        "product_ids": ["agents_api","agents_sdk","dots"],
        "api_capabilities": ["webhooks","developer_tools"],
    },
    "CODEX_AND_DEVELOPER_EXECUTION": {
        "name": "Codex and Developer Execution",
        "purpose": "Coding-agent product metadata and supported developer execution surfaces.",
        "product_ids": ["codex","sdk_libraries"],
        "api_capabilities": ["developer_tools"],
    },
    "APP_AND_EMBEDDED_EXPERIENCES": {
        "name": "Apps and Embedded Experiences",
        "purpose": "ChatGPT Apps SDK and ChatKit developer experience metadata.",
        "product_ids": ["apps_sdk","chatkit"],
        "api_capabilities": ["developer_tools"],
    },
    "EXTENSIBILITY_AND_TOOL_INTEGRATION": {
        "name": "Extensibility and Tool Integration",
        "purpose": "Plugin discovery and Model Context Protocol integration metadata.",
        "product_ids": ["plugins_mcp"],
        "api_capabilities": ["developer_tools","webhooks"],
    },
    "MODEL_API_AND_INFERENCE": {
        "name": "Model API and Inference",
        "purpose": "Model discovery, Responses, Chat Completions, embeddings and fine-tuning capability families.",
        "product_ids": [],
        "api_capabilities": ["platform","models","responses","chat_completions","embeddings","fine_tuning"],
    },
    "MULTIMODAL_AND_REALTIME": {
        "name": "Multimodal and Realtime",
        "purpose": "Image, audio and realtime capability families; catalog metadata only.",
        "product_ids": [],
        "api_capabilities": ["images","audio","realtime"],
    },
    "FILES_AND_RETRIEVAL": {
        "name": "Files and Retrieval",
        "purpose": "Files, batch processing and vector-store/retrieval capability metadata.",
        "product_ids": [],
        "api_capabilities": ["files","batch","vector_stores"],
    },
    "SAFETY_EVALUATION_AND_MODERATION": {
        "name": "Safety, Evaluation and Moderation",
        "purpose": "Moderation, evaluation and webhook governance metadata.",
        "product_ids": [],
        "api_capabilities": ["moderation","evaluations","webhooks"],
    },
    "BUSINESS_EDUCATION_AND_ENTERPRISE": {
        "name": "Business, Education and Enterprise",
        "purpose": "Organization, enterprise and institution-specific workspace controls and entitlements.",
        "product_ids": ["chatgpt_business","chatgpt_enterprise","chatgpt_education"],
        "api_capabilities": [],
    },
    "RETIRED_PRODUCT_REFERENCES": {
        "name": "Retired Product References",
        "purpose": "Historical product records retained for traceability and explicitly excluded from active availability.",
        "product_ids": ["sora"],
        "api_capabilities": [],
    },
}


def list_openai_domain_inventory() -> list[dict[str, Any]]:
    """Return every named product with its domain assignments."""
    products = list_openai_core_modules()
    inventory: list[dict[str, Any]] = []
    for product in products:
        domain_ids = [
            domain_id for domain_id, definition in DOMAIN_DEFINITIONS.items()
            if product["id"] in definition["product_ids"]
        ]
        inventory.append({**product, "domain_ids": domain_ids})
    return inventory


def openai_domain_summary() -> dict[str, Any]:
    inventory = list_openai_domain_inventory()
    domains = []
    for domain_id, definition in DOMAIN_DEFINITIONS.items():
        product_ids = set(definition["product_ids"])
        product_count = sum(1 for item in inventory if item["id"] in product_ids)
        domains.append({
            "domain_id": domain_id,
            "name": definition["name"],
            "purpose": definition["purpose"],
            "product_count": product_count,
            "api_capability_count": len(definition["api_capabilities"]),
            "product_ids": list(definition["product_ids"]),
            "api_capabilities": list(definition["api_capabilities"]),
        })
    return {
        "success": True,
        "provider_id": "openai",
        "domain_count": len(domains),
        "product_count": len(inventory),
        "domain_product_memberships": sum(item["product_count"] for item in domains),
        "api_capability_count": len(OPENAI_API_CAPABILITIES),
        "domains": domains,
    }


def validate_openai_domain_catalog() -> tuple[str, ...]:
    errors: list[str] = []
    product_ids = {item["id"] for item in list_openai_core_modules()}
    for domain_id, definition in DOMAIN_DEFINITIONS.items():
        if not definition.get("name") or not definition.get("purpose"):
            errors.append(f"{domain_id}:NAME_AND_PURPOSE_REQUIRED")
        unknown = set(definition.get("product_ids", [])) - product_ids
        if unknown:
            errors.append(f"{domain_id}:UNKNOWN_PRODUCTS:{','.join(sorted(unknown))}")
        unknown_caps = set(definition.get("api_capabilities", [])) - set(OPENAI_API_CAPABILITIES)
        if unknown_caps:
            errors.append(f"{domain_id}:UNKNOWN_API_CAPABILITIES:{','.join(sorted(unknown_caps))}")
    for product_id in product_ids:
        if not any(product_id in d["product_ids"] for d in DOMAIN_DEFINITIONS.values()):
            errors.append(f"{product_id}:NO_DOMAIN_ASSIGNMENT")
    return tuple(errors)


__all__ = [
    "DOMAIN_DEFINITIONS", "list_openai_domain_inventory",
    "openai_domain_summary", "validate_openai_domain_catalog",
]
