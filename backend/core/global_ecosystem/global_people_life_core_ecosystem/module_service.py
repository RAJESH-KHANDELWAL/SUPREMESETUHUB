"""Reusable read-only service for a registered People Life domain or module."""
from __future__ import annotations
from typing import Any
from .catalog import get_people_life_core_catalog
from .domain_catalog import get_people_life_domain, get_people_life_module
from .contracts import CoreResult, Readiness, TenantContext
from .policy import (
    PeopleLifePolicyError, classify_capability, require_tenant_context,
    safe_domain_summary, validate_capability,
)

class PeopleLifeDomainCoreService:
    """Compatibility service accepting a canonical domain ID or module ID."""

    def __init__(self, domain_id: str) -> None:
        domain = get_people_life_domain(domain_id)
        if domain is None:
            module = get_people_life_module(domain_id)
            if module and module.get("domain_ids"):
                domain = get_people_life_domain(module["domain_ids"][0])
        if domain is None:
            raise LookupError(f"PEOPLE_LIFE_DOMAIN_NOT_REGISTERED: {domain_id}")
        self._domain = {
            **domain,
            "enabled": True,
            "capabilities": ["DOMAIN_METADATA_READ", "SERVICE_DISCOVERY_READ"],
        }
        self.ECOSYSTEM_ID = f"PEOPLE-LIFE-DOMAIN-{domain['domain_id']}"

    def describe(self) -> dict[str, Any]:
        return {
            "success": True, **safe_domain_summary(self._domain),
            "core_layer": "GLOBAL_PEOPLE_LIFE_CORE",
            "application_workflows_in_core": False,
            "live_service_verified": False,
        }

    def readiness(self) -> dict[str, Any]:
        return {
            "domain_id": self._domain["domain_id"],
            "status": Readiness.CATALOG_ONLY.value,
            "catalog_ready": True,
            "application_configuration_required": True,
            "live_service": False,
            "api_calls_performed": 0,
        }

    def capabilities(self) -> dict[str, Any]:
        items = self._domain.get("capabilities", [])
        return {
            "success": True, "domain_id": self._domain["domain_id"],
            "count": len(items),
            "capabilities": [
                {"name": item, "authorization_class": classify_capability(item)}
                for item in items
            ],
        }

    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict[str, Any]:
        try:
            require_tenant_context(context)
            validate_capability(self._domain, capability, context)
        except (ValueError, PermissionError, PeopleLifePolicyError) as exc:
            return CoreResult(
                False, self.ECOSYSTEM_ID, "POLICY_DENIED",
                errors=[str(exc)], request_id=getattr(context, "request_id", None),
            ).to_dict()
        return CoreResult(
            True, self.ECOSYSTEM_ID,
            "CORE_POLICY_PASSED_APPLICATION_AUTHORIZATION_STILL_REQUIRED",
            data={
                "capability": capability, "tenant_id": context.tenant_id,
                "actor_id": context.actor_id,
                "authorization_class": classify_capability(capability),
                "workflow_executed": False,
            },
            request_id=context.request_id,
        ).to_dict()
