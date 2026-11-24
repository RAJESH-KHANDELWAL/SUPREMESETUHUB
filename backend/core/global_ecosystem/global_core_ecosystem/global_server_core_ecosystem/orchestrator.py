"""Offline discovery and readiness orchestration for SERVER CORE."""
from __future__ import annotations

from .catalog import get_catalog
from .constants import ECOSYSTEM_ID
from .manager import get_manager
from .provider_catalog import get_provider, get_provider_catalog, provider_summary


class ServerCoreOrchestrator:
    def catalog(self):
        return get_catalog()

    def providers(self):
        return get_provider_catalog()

    def provider(self, provider_id):
        return get_provider(provider_id)

    def domains(self):
        return get_manager().list_domains()

    def domain(self, domain_id):
        return get_manager().get_domain(domain_id)

    def master_catalog_alignment(self):
        return get_manager().master_catalog_alignment()

    def health(self):
        result = get_manager().status()
        return {
            **result,
            "ecosystem_id": ECOSYSTEM_ID,
            "provider_summary": provider_summary(),
            "remote_operations_enabled": False,
            "api_calls_performed": 0,
        }

    def dependency_map(self):
        return {
            "success": True,
            "edges": [
                {
                    "provider_id": provider["provider_id"],
                    "core_module": (
                        "backend/core/global_ecosystem/global_core_ecosystem/"
                        f"global_server_core_ecosystem/{provider['folder']}"
                    ),
                    "relationship": "SERVER_PROVIDER_METADATA",
                    "live_connection_verified": False,
                }
                for provider in get_provider_catalog()
            ],
        }
