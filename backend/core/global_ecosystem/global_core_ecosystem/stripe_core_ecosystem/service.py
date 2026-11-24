"""Stripe Core Ecosystem read-only control-plane service."""
from __future__ import annotations

from typing import Any

from .catalog import get_stripe_core_catalog, list_stripe_core_modules
from .domain_catalog import stripe_domain_summary
from .master_catalog import get_master_catalog_status
from .orchestrator import StripeCoreOrchestrator
from .policy import StripeCorePolicy


class StripeCoreEcosystemService:
    NAME = "STRIPE CORE ECOSYSTEM"

    def __init__(self) -> None:
        self.orchestrator = StripeCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        catalog = get_stripe_core_catalog()
        modules = list_stripe_core_modules(include_disabled=True)
        health = self.orchestrator.health()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "name": self.NAME,
            "provider": "stripe",
            "status": catalog["status"],
            "enabled": bool(catalog.get("enabled", True)),
            "module_count": len(modules),
            "connected_modules": sum(module.get("connected") is True for module in modules),
            "domain_count": stripe_domain_summary()["domain_count"],
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "api_catalog_ref": catalog["api_catalog_ref"],
            "health": health,
            "master_catalog": get_master_catalog_status(),
        }

    def list_modules(self, include_disabled: bool = False) -> dict[str, Any]:
        modules = list_stripe_core_modules(include_disabled=include_disabled)
        safe = [StripeCorePolicy.safe_metadata(module) for module in modules]
        return {"success": True, "count": len(safe), "modules": safe}

    def get_module(self, module_id: str) -> dict[str, Any] | None:
        return self.orchestrator.get_product(module_id)

    def list_domains(self) -> dict[str, Any]:
        return self.orchestrator.domains()

    def list_registered_modules(self) -> dict[str, Any]:
        """Report package catalog registrations, not live Stripe connections."""
        modules = self.list_modules()["modules"]
        return {
            "success": True,
            "count": len(modules),
            "modules": modules,
            "registration_source": "STRIPE_CORE_CATALOG",
            "live_connection_verified": False,
        }

    def health(self) -> dict[str, Any]:
        return self.orchestrator.health()

    def dependency_map(self) -> dict[str, Any]:
        return self.orchestrator.dependency_map()


__all__ = ["StripeCoreEcosystemService"]
