"""Read-only catalogue service; it performs no external provider calls."""
from datetime import datetime, timezone

from .catalog import ARCHITECTURE, CAPABILITIES, INTEGRATIONS, MODEL_REGISTRY, PROVIDERS, SERVICES, TOOLS


class EcosystemService:
    ECOSYSTEM_ID = "global-ai"
    ECOSYSTEM_NAME = "GLOBAL AI API ECOSYSTEM"
    VERSION = "2.0.0"

    def get_status(self):
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "ecosystem_name": self.ECOSYSTEM_NAME,
            "version": self.VERSION,
            "status": "catalog_ready",
            "implementation_status": "CATALOG_AND_CONTRACTS_READY",
            "runtime_execution_enabled": False,
            "provider_count": len(PROVIDERS),
            "connected_provider_count": 0,
            "capability_count": len(CAPABILITIES),
            "service_count": len(SERVICES),
            "tool_count": len(TOOLS),
            "integration_count": len(INTEGRATIONS),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    @staticmethod
    def _copy(items):
        return [dict(item) for item in items]

    def list_providers(self):
        return self._copy(PROVIDERS)

    def get_provider(self, provider_id: str):
        key = provider_id.strip().casefold()
        return next((dict(item) for item in PROVIDERS if item["provider_id"] == key), None)

    def search_providers(self, query: str):
        term = query.strip().casefold()
        return [dict(item) for item in PROVIDERS if term in item["provider_id"] or term in item["provider_name"].casefold() or term in item["provider_type"]]

    def list_capabilities(self):
        return self._copy(CAPABILITIES)

    def list_services(self):
        return self._copy(SERVICES)

    def list_tools(self):
        return self._copy(TOOLS)

    def list_integrations(self):
        return self._copy(INTEGRATIONS)

    def list_architecture(self):
        return self._copy(ARCHITECTURE)

    def get_models(self):
        return dict(MODEL_REGISTRY)
