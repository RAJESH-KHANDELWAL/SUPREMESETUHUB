"""Canonical Cohere capability domain taxonomy."""
from __future__ import annotations

from .catalog import CAPABILITIES

DOMAIN_DEFINITIONS = {
    "language_understanding": {
        "name": "Language Understanding",
        "description": "Text classification and relevance ranking contracts.",
        "capabilities": ("classify", "rerank"),
    },
    "text_generation": {
        "name": "Text Generation",
        "description": "Command and conversational generation request contracts.",
        "capabilities": ("command",),
    },
    "vector_representation": {
        "name": "Vector Representation",
        "description": "Text embedding and vector representation contracts.",
        "capabilities": ("embed",),
    },
    "text_processing": {
        "name": "Text Processing",
        "description": "Tokenization and text preprocessing contracts.",
        "capabilities": ("tokenize",),
    },
}


def list_domains():
    return {
        domain: tuple(capabilities["capabilities"])
        for domain, capabilities in DOMAIN_DEFINITIONS.items()
    }


def list_domain_inventory():
    return [
        {
            "id": domain,
            "name": metadata["name"],
            "description": metadata["description"],
            "capabilities": list(metadata["capabilities"]),
            "capability_count": len(metadata["capabilities"]),
        }
        for domain, metadata in DOMAIN_DEFINITIONS.items()
    ]


def domain_summary():
    inventory = list_domain_inventory()
    return {
        "domain_count": len(inventory),
        "capability_count": sum(item["capability_count"] for item in inventory),
        "domains": inventory,
        "unassigned_capabilities": sorted(set(CAPABILITIES) - {
            capability
            for item in inventory
            for capability in item["capabilities"]
        }),
    }
