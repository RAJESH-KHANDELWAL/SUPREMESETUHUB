"""API-facing read-only bridge to the canonical Global AI domain registry.

This layer exposes metadata only. It never executes models or returns secrets.
"""
from backend.global_ecosystem.global_ai_ecosystem.providers import (
    get_ai_provider, list_ai_providers, validate_provider_registry,
)
from backend.global_ecosystem.global_ai_ecosystem.adapters.factory import list_chat_adapter_provider_ids
from backend.global_ecosystem.global_ai_ecosystem.capabilities import (
    list_ai_capability_groups, list_ai_modalities,
)
from backend.global_ecosystem.global_ai_ecosystem.scope import (
    get_scope_catalog, list_domain_ids,
)
from backend.global_ecosystem.global_ai_ecosystem.governance import evaluate_use_context


class AIRegistryAPIService:
    """Translate domain registry records into safe API response dictionaries."""

    @staticmethod
    def _adapter_ids() -> set[str]:
        return set(list_chat_adapter_provider_ids())

    def list_providers(self, *, category=None, integration_status=None):
        adapter_ids = self._adapter_ids()
        records = list_ai_providers(category=category, integration_status=integration_status)
        return [
            {
                "provider_id": item["id"],
                "provider_name": item["name"],
                "provider_type": item["category"],
                "catalog_path": "backend/global_ecosystem/global_ai_ecosystem/providers.py",
                "integration_status": item.get("integration_status", "catalog_only"),
                "chat_adapter_available": item["id"] in adapter_ids,
                "live_connection_verified": False,
                "models_or_services": list(item.get("models_or_services", [])),
            }
            for item in records
        ]

    def get_provider(self, provider_id: str):
        item = get_ai_provider(provider_id)
        if item is None:
            return None
        return next((record for record in self.list_providers() if record["provider_id"] == item["id"]), None)

    def list_categories(self):
        counts = {}
        for item in list_ai_providers():
            category = item.get("category", "uncategorized")
            counts[category] = counts.get(category, 0) + 1
        return [{"category": key, "count": counts[key]} for key in sorted(counts)]

    def list_adapters(self):
        ids = self._adapter_ids()
        return {
            "count": len(ids),
            "provider_ids": sorted(ids),
            "live_connections_verified": False,
            "note": "Adapter code is available; credentials and live connectivity are not implied.",
        }

    def get_registry_validation(self):
        errors = list(validate_provider_registry())
        return {"valid": not errors, "error_count": len(errors), "errors": errors}

    def list_capabilities(self):
        return {
            "modalities": list_ai_modalities(),
            "groups": list_ai_capability_groups(),
        }

    def list_domains(self):
        return get_scope_catalog()

    def policy_precheck(self, payload):
        return evaluate_use_context(**payload)
