"""Read-only discovery and dependency orchestration for Developer Core."""
from __future__ import annotations
from .catalog import get_developer_core_catalog, get_developer_core_provider

DEPENDENCIES = {
    "api": "backend/api/global_ecosystem/global_api_ecosystem/global_developer_api_ecosystem",
    "engine": "backend/engine/global_ecosystem/global_engine_ecosystem/global_developer_engine_ecosystem",
    "database": "backend/database/global_ecosystem/global_database_ecosystem",
    "storage": "backend/storage/global_ecosystem/global_storage_ecosystem",
    "security_identity": "backend/security",
    "application": "backend/application",
}

class GlobalDeveloperCoreOrchestrator:
    def catalog(self):
        return get_developer_core_catalog()

    def provider(self, provider_id):
        return get_developer_core_provider(provider_id)

    def dependency_map(self):
        return dict(DEPENDENCIES)

    def health(self):
        catalog = self.catalog()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "provider_count": catalog["provider_count"],
            "registered": True,
            "live_connection_verified": False,
            "external_api_calls": 0,
            "status": "CORE_CATALOG_ONLY",
        }
