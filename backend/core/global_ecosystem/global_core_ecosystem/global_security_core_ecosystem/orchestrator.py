"""Global Security Core discovery and readiness orchestration.

The orchestrator composes local catalog metadata only. It performs no provider
network calls, security scans, incident response or runtime enforcement.
"""
from __future__ import annotations

from typing import Any

from .catalog import (
    get_catalog,
    get_security_core_catalog,
    list_security_core_modules,
)
from .constants import ECOSYSTEM_ID, STATUS
from .content_safety_policy import content_safety_baseline
from .domain_catalog import get_domain, get_domains, domain_summary
from .jurisdiction_catalog import (
    get_jurisdiction,
    get_jurisdictions,
    jurisdiction_summary,
)
from .provider_catalog import (
    get_provider,
    get_provider_catalog,
    provider_summary,
)


class SecurityCoreOrchestrator:
    """Provide read-only discovery, health and dependency summaries."""

    def catalog(self) -> dict[str, Any]:
        return get_catalog()

    def registry(self) -> dict[str, Any]:
        return get_security_core_catalog()

    def list_modules(self, enabled_only: bool = False) -> dict[str, Any]:
        items = list_security_core_modules(include_disabled=not enabled_only)
        return {"success": True, "count": len(items), "modules": items}

    def list_providers(self) -> list[dict[str, Any]]:
        return get_provider_catalog()

    def get_provider(self, provider_id: str) -> dict[str, Any] | None:
        return get_provider(provider_id)

    def list_domains(self) -> list[dict[str, Any]]:
        return get_domains()

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return get_domain(domain_id)

    def list_jurisdictions(self) -> list[dict[str, Any]]:
        return get_jurisdictions()

    def get_jurisdiction(self, jurisdiction_id: str) -> dict[str, Any] | None:
        return get_jurisdiction(jurisdiction_id)

    def content_safety(self) -> dict[str, Any]:
        return content_safety_baseline()

    def health(self) -> dict[str, Any]:
        return {
            "success": True,
            "ecosystem_id": ECOSYSTEM_ID,
            "status": STATUS,
            **domain_summary(),
            **provider_summary(),
            **jurisdiction_summary(),
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "security_enforcement_verified": False,
            "legal_compliance_verified": False,
            "warning": (
                "Catalog registration does not prove provider credentials, API "
                "availability, protection coverage, live connectivity or legal compliance."
            ),
        }

    def dependency_map(self) -> dict[str, Any]:
        return {
            "success": True,
            "edges": [
                {
                    "provider_id": item["provider_id"],
                    "core_module": (
                        "backend/core/global_ecosystem/global_core_ecosystem/"
                        f"global_security_core_ecosystem/{item['folder']}"
                    ),
                    "relationship": "PROVIDER_SECURITY_METADATA",
                    "live_connection_verified": False,
                }
                for item in get_provider_catalog()
            ],
        }
