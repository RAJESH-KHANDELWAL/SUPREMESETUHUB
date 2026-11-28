"""Communication Core policy boundaries. No provider actions are executed here."""
from __future__ import annotations
from typing import Any

class CommunicationPolicyError(PermissionError):
    pass

RESTRICTED_KINDS = {"restricted_domain", "restricted_directory", "sensitive_domain"}
SENSITIVE_CAPABILITIES = {"SEND_MESSAGE", "SEND_EMAIL", "PLACE_CALL", "EXPORT_CONTACTS", "READ_PRIVATE_CONTENT", "MODERATE_CONTENT"}

class CommunicationCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None or not callable(getattr(context, "validate", None)):
            raise CommunicationPolicyError("VALIDATED_TENANT_CONTEXT_REQUIRED")
        context.validate()

    @staticmethod
    def classify_product(product: dict[str, Any]) -> str:
        if product.get("kind") in RESTRICTED_KINDS:
            return "RESTRICTED_REQUIRES_AGE_CONSENT_AND_LEGAL_REVIEW"
        return "STANDARD_METADATA_ONLY"

    @staticmethod
    def require_explicit_authorization(capability: str, authorized: bool) -> None:
        if capability in SENSITIVE_CAPABILITIES and not authorized:
            raise CommunicationPolicyError("EXPLICIT_AUTHORIZATION_REQUIRED")

    @staticmethod
    def safe_summary(record: dict[str, Any]) -> dict[str, Any]:
        blocked = {"token", "access_token", "refresh_token", "client_secret", "api_key", "secret", "phone_number", "email_address"}
        return {key: value for key, value in record.items() if key.casefold() not in blocked}
__all__ = ["CommunicationCorePolicy", "CommunicationPolicyError"]
