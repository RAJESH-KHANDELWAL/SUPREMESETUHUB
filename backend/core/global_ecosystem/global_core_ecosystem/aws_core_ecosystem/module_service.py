"""Shared read-only Core service for AWS service families."""
from __future__ import annotations
from typing import Any
from .catalog import get_aws_core_catalog
from .contracts import AwsAccountContext, CoreResult, Readiness
from .policy import AwsCorePolicy

class AwsProductCoreService:
    ECOSYSTEM_ID = ""
    def __init__(self) -> None:
        if not self.ECOSYSTEM_ID:
            raise NotImplementedError("Product service must define ECOSYSTEM_ID")
        self._module = next((item for item in get_aws_core_catalog()["children"] if item["ecosystem_id"] == self.ECOSYSTEM_ID), None)
        if self._module is None:
            raise LookupError(f"AWS_CORE_MODULE_NOT_REGISTERED: {self.ECOSYSTEM_ID}")

    def _readiness(self) -> str:
        if not self._module.get("enabled", True):
            return Readiness.DISABLED.value
        return self._module.get("status", Readiness.CATALOG_ONLY.value)

    def status(self) -> dict[str, Any]:
        return {"success": True, **AwsCorePolicy.safe_module_summary(self._module), "provider": "aws", "core_layer": "AWS_CORE", "readiness": self._readiness(), "api_transport_in_core": False, "live_connection_verified": False}

    def capabilities(self) -> dict[str, Any]:
        caps = self._module.get("capabilities", [])
        return {"success": True, "ecosystem_id": self.ECOSYSTEM_ID, "count": len(caps), "capabilities": [{"name": cap, "authorization_class": AwsCorePolicy.classify_capability(cap)} for cap in caps]}

    def authorize_capability(self, capability: str, context: AwsAccountContext | None) -> dict[str, Any]:
        try:
            AwsCorePolicy.require_account_context(context)
            AwsCorePolicy.validate_capability(self._module, capability)
        except (ValueError, PermissionError) as exc:
            return CoreResult(False, self.ECOSYSTEM_ID, "POLICY_DENIED", errors=[str(exc)], request_id=getattr(context, "request_id", None)).to_dict()
        return CoreResult(True, self.ECOSYSTEM_ID, "CORE_POLICY_PASSED_IAM_AUTH_STILL_REQUIRED", data={"capability": capability, "account_id": context.account_id, "region": context.region, "tenant_id": context.tenant_id, "actor_id": context.actor_id, "iam_authorization_performed": False, "aws_api_call_performed": False}, request_id=context.request_id).to_dict()
