"""Metadata-only safety and authorization guardrails for GLOBAL VIDEO CORE ECOSYSTEM."""
from __future__ import annotations
from typing import Any

SENSITIVE_MARKERS = ("ADMIN", "DELETE", "WRITE", "UPLOAD", "PUBLISH", "BILLING", "PAYMENT", "MODERATE", "VERIFY", "LICENSE", "CONSENT", "PRIVATE", "EXPORT")
BLOCKED_FIELDS = {"token", "access_token", "refresh_token", "client_secret", "api_key", "secret", "private_media", "private_url"}
class CorePolicyError(PermissionError): pass

def require_tenant_context(context: Any) -> None:
    if context is None or not callable(getattr(context, "validate", None)): raise CorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
    context.validate()

def classify_capability(capability: str) -> str:
    value = capability.upper()
    return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION_AND_AUDIT" if any(x in value for x in SENSITIVE_MARKERS) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"

def safe_metadata(record: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in record.items() if k.casefold() not in BLOCKED_FIELDS}

def validate_provider(provider: dict[str, Any]) -> None:
    from .domain_catalog import DOMAIN_DEFINITIONS
    if provider.get("domain_id") not in DOMAIN_DEFINITIONS: raise ValueError("UNKNOWN_DOMAIN_ID")
    if not provider.get("provider_id") or not provider.get("name"): raise ValueError("PROVIDER_IDENTITY_REQUIRED")
    if provider.get("connected") is True or provider.get("live_connection_verified") is True: raise ValueError("CORE_CATALOG_CANNOT_ASSERT_LIVE_CONNECTION")
