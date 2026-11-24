"""Shared read-only service for all Stripe child Core packages."""
from __future__ import annotations

from typing import Any

from .catalog import list_stripe_core_modules
from .policy import StripeCorePolicy


class StripeModuleCoreService:
    """Resolve one registered family without duplicating 22 child managers."""

    def __init__(self, module_id: str) -> None:
        self.module_id = module_id

    def _module(self) -> dict[str, Any] | None:
        needle = self.module_id.strip().casefold()
        if not needle:
            return None
        for module in list_stripe_core_modules(include_disabled=True):
            if needle in {
                module["ecosystem_id"].casefold(),
                module["module"].casefold(),
                module["api_family"].casefold(),
            }:
                return StripeCorePolicy.safe_metadata(module)
        return None

    def status(self) -> dict[str, Any]:
        module = self._module()
        if module is None:
            return {"success": False, "status": "NOT_REGISTERED", "module": None}
        return {
            "success": True,
            "status": module["status"],
            "module": module,
            "live_connection_verified": False,
        }

    def validate_capability(self, capability: str) -> dict[str, Any]:
        module = self._module()
        if module is None:
            return {"success": False, "error": "MODULE_NOT_REGISTERED"}
        StripeCorePolicy.validate_capability(module, capability)
        return {
            "success": True,
            "module_id": module["ecosystem_id"],
            "capability": capability,
            "policy_classification": StripeCorePolicy.classify_capability(capability),
            "authorization_verified": False,
            "api_call_performed": False,
        }


__all__ = ["StripeModuleCoreService"]
