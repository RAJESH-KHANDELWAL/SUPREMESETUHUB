"""Fail-closed policy helpers for Twilio Core metadata."""
from __future__ import annotations
from .contracts import TenantContext

class TwilioCorePolicy:
    SENSITIVE_CAPABILITIES = {
        "MESSAGING_SEND", "VOICE_CALL_INITIATE", "VIDEO_ROOM_CREATE",
        "VERIFY_START", "VERIFY_CHECK", "PHONE_NUMBER_PURCHASE",
        "PHONE_NUMBER_CONFIGURATION", "BILLING_CHANGE",
    }

    @staticmethod
    def validate_tenant(context: TenantContext) -> None:
        if not isinstance(context, TenantContext):
            raise TypeError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        context.validate()

    @classmethod
    def authorize_metadata_capability(cls, capability: str, context: TenantContext) -> dict:
        cls.validate_tenant(context)
        normalized = str(capability).strip().upper()
        if not normalized:
            raise ValueError("CAPABILITY_REQUIRED")
        if normalized in cls.SENSITIVE_CAPABILITIES:
            return {
                "allowed": False,
                "status": "RUNTIME_AUTHORIZATION_REQUIRED",
                "reason": "Core metadata does not authorize provider-side communication or billing actions.",
                "api_call_performed": False,
            }
        return {
            "allowed": True,
            "status": "CORE_METADATA_POLICY_PASSED",
            "tenant_id": context.tenant_id,
            "capability": normalized,
            "provider_authorization_still_required": True,
            "api_call_performed": False,
        }
