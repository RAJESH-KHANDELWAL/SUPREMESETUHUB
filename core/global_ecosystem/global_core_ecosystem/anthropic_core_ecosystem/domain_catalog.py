"""Anthropic Core domain taxonomy over registered product families.

Classification is metadata only. It does not assert API access or capability
availability for any Anthropic account or workspace.
"""
from __future__ import annotations

from collections import Counter
from typing import Any

from .catalog import list_anthropic_core_modules

DOMAIN_DEFINITIONS: dict[str, dict[str, str]] = {
    "MESSAGING_AND_CONVERSATION": {
        "name": "Messaging and Conversation",
        "purpose": "Message creation, conversational requests, streaming and response lifecycle.",
    },
    "BATCH_PROCESSING": {
        "name": "Batch Processing",
        "purpose": "Asynchronous message batch submission, status and result metadata.",
    },
    "MODEL_DISCOVERY_AND_METADATA": {
        "name": "Model Discovery and Metadata",
        "purpose": "Model identity, catalog metadata and model capability classification.",
    },
    "TOKEN_ACCOUNTING": {
        "name": "Token Counting",
        "purpose": "Input token estimation and token-counting capability metadata.",
    },
    "FILE_ASSETS": {
        "name": "File Assets",
        "purpose": "Provider file capability metadata and file lifecycle policy boundaries.",
    },
    "WORKSPACE_GOVERNANCE": {
        "name": "Workspace Governance",
        "purpose": "Administrative workspace identity, membership and governance boundaries.",
    },
    "MANAGED_AGENT_OPERATIONS": {
        "name": "Managed Agent Operations",
        "purpose": "Managed agent sessions and environment capability metadata.",
    },
    "TOOL_INTERACTION": {
        "name": "Tool Interaction",
        "purpose": "Tool definitions, tool-choice metadata and handoff boundaries.",
    },
    "AUTHENTICATION_AND_IDENTITY": {
        "name": "Authentication and Identity",
        "purpose": "Credential readiness, workload identity and credential lifecycle boundaries.",
    },
}

PRODUCT_DOMAIN: dict[str, str] = {
    "messages": "MESSAGING_AND_CONVERSATION",
    "batches": "BATCH_PROCESSING",
    "models": "MODEL_DISCOVERY_AND_METADATA",
    "token_counting": "TOKEN_ACCOUNTING",
    "files": "FILE_ASSETS",
    "admin_workspaces": "WORKSPACE_GOVERNANCE",
    "managed_agents": "MANAGED_AGENT_OPERATIONS",
    "tool_use": "TOOL_INTERACTION",
    "auth_identity": "AUTHENTICATION_AND_IDENTITY",
}


def list_anthropic_domain_inventory() -> list[dict[str, Any]]:
    inventory: list[dict[str, Any]] = []
    for product in list_anthropic_core_modules():
        product_id = str(product.get("product_id", ""))
        domain_id = PRODUCT_DOMAIN.get(product_id)
        definition = DOMAIN_DEFINITIONS.get(domain_id or "", {})
        inventory.append({
            **product,
            "core_domain_id": domain_id or "SPECIALTY_AND_CROSS_PRODUCT",
            "core_domain_name": definition.get("name", "Specialty and Cross-product"),
            "domain_assignment": "PRODUCT_RULE" if domain_id else "SPECIALTY_REVIEW_REQUIRED",
        })
    return inventory


def anthropic_domain_summary() -> dict[str, Any]:
    inventory = list_anthropic_domain_inventory()
    counts = Counter(item["core_domain_id"] for item in inventory)
    unmapped = sorted(
        str(item.get("product_id", ""))
        for item in inventory
        if item["domain_assignment"] != "PRODUCT_RULE"
    )
    return {
        "success": True,
        "domain_count": len(DOMAIN_DEFINITIONS),
        "offering_count": len(inventory),
        "assigned_offering_count": len(inventory) - len(unmapped),
        "unmapped_products": unmapped,
        "domains": [
            {"domain_id": domain_id, **definition, "offering_count": counts.get(domain_id, 0)}
            for domain_id, definition in DOMAIN_DEFINITIONS.items()
        ],
        "live_connections_verified": 0,
        "note": "Domain assignment is Core classification only; it is not API availability, entitlement, authorization or live connectivity.",
    }
