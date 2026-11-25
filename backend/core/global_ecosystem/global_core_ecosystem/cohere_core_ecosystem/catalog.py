"""Canonical Cohere provider CORE catalog.

This is metadata and capability routing only; it does not call Cohere APIs.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

PROVIDER = "cohere"
LAYER = "CORE"
STATUS = "interface_only"

_CAPABILITY_DEFINITIONS: dict[str, dict[str, Any]] = {
    "classify": {
        "package": "cohere_classify_core_ecosystem",
        "name": "Cohere Classify",
        "description": "Text classification request contract and readiness metadata.",
        "domain": "language_understanding",
    },
    "command": {
        "package": "cohere_command_core_ecosystem",
        "name": "Cohere Command",
        "description": "Text generation and conversational request contract metadata.",
        "domain": "text_generation",
    },
    "embed": {
        "package": "cohere_embed_core_ecosystem",
        "name": "Cohere Embed",
        "description": "Text embedding request contract and vector representation metadata.",
        "domain": "vector_representation",
    },
    "rerank": {
        "package": "cohere_rerank_core_ecosystem",
        "name": "Cohere Rerank",
        "description": "Query/document relevance ranking request contract metadata.",
        "domain": "language_understanding",
    },
    "tokenize": {
        "package": "cohere_tokenize_core_ecosystem",
        "name": "Cohere Tokenize",
        "description": "Text tokenization request contract metadata.",
        "domain": "text_processing",
    },
}

CAPABILITIES: dict[str, dict[str, Any]] = {
    capability: {
        **metadata,
        "module": metadata["package"],
        "mode": "contract_only",
        "status": "CORE_CONTRACT_ONLY",
        "live_enabled": False,
    }
    for capability, metadata in _CAPABILITY_DEFINITIONS.items()
}

COHERE_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "COHERE-CORE-ECOSYSTEM",
    "name": "COHERE CORE ECOSYSTEM",
    "provider": PROVIDER,
    "ecosystem_type": "PROVIDER_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "INTERFACE_ONLY",
    "enabled": True,
    "api_catalog_ref": (
        "backend/api/global_ecosystem/global_api_ecosystem/"
        "cohere_api_ecosystem"
    ),
    "engine_ref": (
        "backend/engine/global_ecosystem/global_engine_ecosystem/"
        "cohere_engine_ecosystem"
    ),
    "capabilities": [
        "COHERE_PROVIDER_CORE_REGISTRY",
        "COHERE_CLASSIFY_CORE",
        "COHERE_COMMAND_CORE",
        "COHERE_EMBED_CORE",
        "COHERE_RERANK_CORE",
        "COHERE_TOKENIZE_CORE",
        "CAPABILITY_CONTRACT_VALIDATION",
        "TENANT_CONTEXT_BOUNDARY",
        "SECRET_REFERENCE_BOUNDARY",
        "READINESS_AND_LIFECYCLE_METADATA",
    ],
    "children": [
        {
            "ecosystem_id": f"COHERE-{capability.upper()}-CORE-ECOSYSTEM",
            "name": metadata["name"].upper() + " CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_CORE_CAPABILITY",
            "parent_id": "COHERE-CORE-ECOSYSTEM",
            "capability": capability,
            "capabilities": [capability.upper()],
            "core_module": (
                "backend/core/global_ecosystem/global_core_ecosystem/"
                f"cohere_core_ecosystem/{metadata['package']}"
            ),
            "api_catalog_ref": (
                "backend/api/global_ecosystem/global_api_ecosystem/"
                "cohere_api_ecosystem"
            ),
            "engine_ref": (
                "backend/engine/global_ecosystem/global_engine_ecosystem/"
                "cohere_engine_ecosystem"
            ),
            "status": "CORE_CONTRACT_ONLY",
            "enabled": True,
            "connected": False,
            "live_connection_verified": False,
        }
        for capability, metadata in _CAPABILITY_DEFINITIONS.items()
    ],
}


def get_cohere_core_catalog() -> dict[str, Any]:
    """Return a defensive copy of the provider and capability catalog."""
    return deepcopy(COHERE_CORE_ECOSYSTEM)


def list_cohere_core_modules(*, enabled_only: bool = False) -> list[dict[str, Any]]:
    """Return registered capability modules without secret or runtime data."""
    modules = deepcopy(COHERE_CORE_ECOSYSTEM["children"])
    if enabled_only:
        modules = [item for item in modules if item.get("enabled", True)]
    return modules


def list_capabilities() -> dict[str, dict[str, Any]]:
    """Return a defensive copy of the canonical five-capability inventory."""
    return deepcopy(CAPABILITIES)
