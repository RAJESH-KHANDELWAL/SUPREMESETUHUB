"""Canonical Global Developer Core provider and domain catalog."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

ECOSYSTEM_ID = "GLOBAL-DEVELOPER-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL DEVELOPER CORE ECOSYSTEM"
PARENT_ID = "GLOBAL-CORE-ECOSYSTEM"
LAYER = "CORE"
API_ROOT = "backend/api/global_ecosystem/global_api_ecosystem/global_developer_api_ecosystem"
CORE_ROOT = "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem"

# Mirrors provider-specific API package directories; support namespaces are excluded.
PROVIDER_PACKAGES: tuple[str, ...] = (
    "adult_creator_business",
    "adult_platform_discovery",
    "age_verification_consent",
    "ai_ml_data",
    "anthropic_developer",
    "apple_developer",
    "atlassian_developer",
    "aws_developer",
    "blockchain_web3",
    "cohere_developer",
    "content_moderation_safety",
    "database_storage",
    "dating_relationships",
    "deepseek_developer",
    "developer_security_compliance",
    "github_developer",
    "global_cloud_infrastructure",
    "google_developer",
    "huggingface_developer",
    "identity_authentication",
    "india_developer_platform",
    "microsoft_developer",
    "mistral_developer",
    "no_code_automation",
    "nvidia_developer",
    "openai_developer",
    "payments_billing",
    "sexual_wellness_education",
    "testing_observability",
)

def _record(provider_id: str) -> dict[str, Any]:
    package = f"{provider_id}_core_ecosystem"
    api_package = f"{provider_id}_api_ecosystem"
    return {
        "provider_id": provider_id,
        "ecosystem_id": f"GLOBAL-DEVELOPER-{provider_id.upper().replace('_', '-')}-CORE-ECOSYSTEM",
        "name": f"{provider_id.replace('_', ' ').upper()} CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "parent_id": ECOSYSTEM_ID,
        "core_module": f"{CORE_ROOT}/{package}",
        "api_catalog_ref": f"{API_ROOT}/{api_package}",
        "capabilities": ["PROVIDER_DISCOVERY", "CAPABILITY_METADATA", "LIFECYCLE_METADATA"],
        "status": "CORE_CATALOG_ONLY",
        "connected": False,
        "live_connection_verified": False,
        "api_available": None,
    }

PROVIDER_CATALOG: tuple[dict[str, Any], ...] = tuple(_record(x) for x in PROVIDER_PACKAGES)

def get_developer_core_catalog() -> dict[str, Any]:
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": ECOSYSTEM_NAME,
        "ecosystem_type": "CORE",
        "parent_id": PARENT_ID,
        "status": "REGISTERED",
        "enabled": True,
        "api_catalog_root": API_ROOT,
        "provider_count": len(PROVIDER_CATALOG),
        "providers": deepcopy(list(PROVIDER_CATALOG)),
    }

def list_developer_core_providers() -> list[dict[str, Any]]:
    return deepcopy(list(PROVIDER_CATALOG))

def get_developer_core_provider(provider_id: str) -> dict[str, Any] | None:
    normalized = str(provider_id).strip().lower()
    for record in PROVIDER_CATALOG:
        if record["provider_id"] == normalized or record["ecosystem_id"] == normalized.upper():
            return deepcopy(record)
    return None
