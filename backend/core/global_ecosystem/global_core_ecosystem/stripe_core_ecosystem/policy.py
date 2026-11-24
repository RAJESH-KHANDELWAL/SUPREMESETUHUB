"""Stripe Core policy guardrails; not a substitute for API authorization."""
from __future__ import annotations

from typing import Any

SENSITIVE_MARKERS = (
    "WRITE", "CREATE", "CONFIRM", "CAPTURE", "CANCEL", "REFUND", "PAYOUT",
    "TRANSFER", "ISSUE", "DELETE", "ADMIN", "DISPUTE", "TREASURY",
)
SECRET_KEYS = {
    "token", "access_token", "refresh_token", "client_secret", "api_key",
    "secret", "stripe_secret_key", "webhook_secret", "authorization",
    "pan", "cvc", "card_number",
}


class StripeCorePolicyError(PermissionError):
    """Raised when Core metadata or caller context violates policy."""


class StripeCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None:
            raise StripeCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator = getattr(context, "validate", None)
        if not callable(validator):
            raise StripeCorePolicyError("INVALID_TENANT_CONTEXT")
        try:
            validator()
        except (TypeError, ValueError) as exc:
            raise StripeCorePolicyError(str(exc)) from exc

    @staticmethod
    def validate_capability(module: dict[str, Any], capability: str) -> None:
        if not module.get("enabled", True) or module.get("status") == "DISABLED":
            raise StripeCorePolicyError("MODULE_DISABLED")
        if capability not in set(module.get("capabilities", [])):
            raise StripeCorePolicyError("CAPABILITY_NOT_REGISTERED")
        # Registration never proves Stripe entitlement, API authorization or
        # the caller's permission to perform a payment operation.

    @staticmethod
    def classify_capability(capability: str) -> str:
        upper = capability.upper()
        if any(marker in upper for marker in SENSITIVE_MARKERS):
            return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION_AND_AUDIT"
        return "STANDARD_REQUIRES_TENANT_AUTHORIZATION"

    @staticmethod
    def require_idempotency_key(key: str | None) -> None:
        if not isinstance(key, str) or not key.strip():
            raise StripeCorePolicyError("IDEMPOTENCY_KEY_REQUIRED_FOR_PAYMENT_WRITE")

    @staticmethod
    def require_verified_webhook(event: dict[str, Any]) -> None:
        if event.get("signature_verified") is not True:
            raise StripeCorePolicyError("WEBHOOK_SIGNATURE_MUST_BE_VERIFIED_IN_API_LAYER")

    @staticmethod
    def safe_metadata(value: Any) -> Any:
        """Recursively remove credential and card-data fields from public output."""
        if isinstance(value, dict):
            return {
                key: StripeCorePolicy.safe_metadata(item)
                for key, item in value.items()
                if str(key).casefold() not in SECRET_KEYS
            }
        if isinstance(value, list):
            return [StripeCorePolicy.safe_metadata(item) for item in value]
        if isinstance(value, tuple):
            return [StripeCorePolicy.safe_metadata(item) for item in value]
        return value


__all__ = ["StripeCorePolicy", "StripeCorePolicyError"]
