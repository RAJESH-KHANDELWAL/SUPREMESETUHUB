"""Metadata-only privacy and capability policy guardrails."""
from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any

SENSITIVE_MARKERS = (
    "IDENTITY", "KYC", "AGE", "HEALTH", "FINANCE", "WALLET",
    "ADULT", "INTIMACY", "CONSENT", "PAYMENT", "PRIVATE",
)
_SENSITIVE_KEY_PARTS = (
    "token", "secret", "password", "authorization", "credential",
    "apikey", "email", "phone", "mobile", "governmentid", "idnumber",
    "medicalrecord", "dateofbirth", "birthdate", "dob", "address",
    "aadhaar", "pannumber", "passportnumber", "bankaccount",
    "cardnumber", "ssn", "privatekey",
)


def _is_sensitive_key(key: object) -> bool:
    normalized = re.sub(r"[^a-z0-9]", "", str(key).casefold())
    return any(marker in normalized for marker in _SENSITIVE_KEY_PARTS)


class GlobalIndividualCorePolicyError(PermissionError):
    """Raised when an Individual Core metadata policy boundary is violated."""


class GlobalIndividualCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None or not callable(getattr(context, "validate", None)):
            raise GlobalIndividualCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        try:
            context.validate()
        except (TypeError, ValueError) as exc:
            raise GlobalIndividualCorePolicyError(str(exc)) from exc

    @staticmethod
    def classify_capability(capability: str) -> str:
        value = str(capability).upper()
        return (
            "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION_CONSENT_AND_AUDIT"
            if any(marker in value for marker in SENSITIVE_MARKERS)
            else "STANDARD_REQUIRES_TENANT_AND_APPLICATION_AUTHORIZATION"
        )

    @staticmethod
    def safe_metadata(value: Any) -> Any:
        if isinstance(value, Mapping):
            return {
                key: GlobalIndividualCorePolicy.safe_metadata(item)
                for key, item in value.items()
                if not _is_sensitive_key(key)
            }
        if isinstance(value, (tuple, list)):
            return [GlobalIndividualCorePolicy.safe_metadata(item) for item in value]
        return value


__all__ = ["GlobalIndividualCorePolicy", "GlobalIndividualCorePolicyError"]
