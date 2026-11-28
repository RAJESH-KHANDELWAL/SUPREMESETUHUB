"""Provider-neutral inventory derived from the canonical Infrastructure Ecosystem."""
from __future__ import annotations

from copy import deepcopy
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.providers import PROVIDERS
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.structure import INFRASTRUCTURE_MODULES

ECOSYSTEM_ID = "GLOBAL-INFRASTRUCTURE-CORE-ECOSYSTEM"

def get_domain_catalog() -> list[dict]:
    return [
        {
            "id": name,
            "name": name.replace("_", " ").title(),
            "source": "GLOBAL_INFRASTRUCTURE_ECOSYSTEM",
            "provider_neutral": True,
        }
        for name in INFRASTRUCTURE_MODULES
    ]

def get_provider_catalog() -> list[dict]:
    return [
        {
            **provider.to_dict(),
            "status": "CATALOG_ONLY",
            "live_connection_verified": False,
        }
        for provider in PROVIDERS
    ]

def get_catalog() -> dict:
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "domains": deepcopy(get_domain_catalog()),
        "providers": deepcopy(get_provider_catalog()),
        "provider_operations_enabled": False,
    }

__all__ = ["ECOSYSTEM_ID", "get_domain_catalog", "get_provider_catalog", "get_catalog"]
