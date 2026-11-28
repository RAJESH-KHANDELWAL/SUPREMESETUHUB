"""Shared read-only product Core service."""
from .catalog import get_ai_provider
from .contracts import CoreResult, Readiness
from .policy import GlobalAICorePolicy


class AIProductCoreService:
    PROVIDER_ID = ""

    def __init__(self):
        if not self.PROVIDER_ID:
            raise NotImplementedError("PROVIDER_ID_REQUIRED")
        self._provider = get_ai_provider(self.PROVIDER_ID)
        if self._provider is None:
            raise LookupError("AI_CORE_PROVIDER_NOT_REGISTERED: " + self.PROVIDER_ID)

    def status(self):
        status = self._provider.get("integration_status")
        readiness = {
            "scaffold": Readiness.ADAPTER_SCAFFOLD.value,
            "integration_in_progress": Readiness.CONFIGURATION_REQUIRED.value,
            # A registry label is not proof of an authenticated live connection.
            "live": Readiness.LIVE_VERIFICATION_REQUIRED.value,
        }.get(status, Readiness.CATALOG_ONLY.value)
        return {
            "success": True,
            **GlobalAICorePolicy.safe_provider_summary(self._provider),
            "core_layer": "GLOBAL_AI_CORE",
            "api_transport_in_core": False,
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "readiness": readiness,
        }

    def capabilities(self):
        items = self._provider.get(
            "capabilities", self._provider.get("models_or_services", [])
        )
        return {
            "success": True,
            "provider_id": self.PROVIDER_ID,
            "count": len(items),
            "capabilities": [
                {
                    "name": item,
                    "authorization_class": GlobalAICorePolicy.classify_capability(
                        str(item)
                    ),
                }
                for item in items
            ],
        }

    def authorize_capability(self, capability, context):
        try:
            GlobalAICorePolicy.require_tenant_context(context)
            GlobalAICorePolicy.validate_capability(self._provider, capability)
        except (ValueError, PermissionError) as exc:
            return CoreResult(
                False,
                self.PROVIDER_ID,
                "POLICY_DENIED",
                errors=[str(exc)],
                request_id=getattr(context, "request_id", None),
            ).to_dict()
        return CoreResult(
            True,
            self.PROVIDER_ID,
            "CORE_POLICY_PASSED_API_AUTH_STILL_REQUIRED",
            data={
                "capability": capability,
                "tenant_id": context.tenant_id,
                "actor_id": context.actor_id,
                "api_call_performed": False,
            },
            request_id=context.request_id,
        ).to_dict()
