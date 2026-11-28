"""AWS Core capability classification; IAM authorization remains in AWS API."""
from __future__ import annotations

from typing import Any

from .contracts import AwsAccountContext

ELEVATED_MARKERS = (
    "IAM", "STS", "KMS", "SECRET", "DELETE", "WRITE", "CREATE",
    "UPDATE", "DEPLOY", "ROTATE", "REVOKE", "BILLING", "COST",
    "POLICY", "NETWORK", "SECURITY_GROUP", "PROVISION",
)


class AwsCorePolicyError(PermissionError):
    """Raised when AWS Core metadata policy rejects a request."""


class AwsCorePolicy:
    """Validate Core metadata and context; never replace AWS IAM authorization."""

    @staticmethod
    def safe_module_summary(module: dict[str, Any]) -> dict[str, Any]:
        """Allow-list public catalog fields; never serialize arbitrary metadata."""
        keys = (
            "ecosystem_id", "name", "ecosystem_type", "parent_id",
            "capabilities", "domains", "status", "enabled", "core_module",
            "api_catalog_ref", "connected", "live_connection_verified",
            "api_available",
        )
        return {key: module[key] for key in keys if key in module}

    @staticmethod
    def classify_capability(capability: str) -> str:
        token = capability.upper()
        if any(marker in token for marker in ELEVATED_MARKERS):
            return "ELEVATED_REQUIRES_EXPLICIT_AUTHORIZATION_AND_AUDIT"
        return "IAM_AND_RESOURCE_POLICY_REQUIRED"

    @staticmethod
    def require_account_context(context: AwsAccountContext | None) -> None:
        if context is None:
            raise AwsCorePolicyError("AWS_ACCOUNT_CONTEXT_REQUIRED")
        context.validate()

    @staticmethod
    def validate_capability(module: dict[str, Any], capability: str) -> None:
        if not module.get("enabled", True):
            raise AwsCorePolicyError("AWS_CORE_MODULE_DISABLED")
        if not isinstance(capability, str) or not capability.strip():
            raise AwsCorePolicyError("AWS_CAPABILITY_REQUIRED")
        if capability not in module.get("capabilities", []):
            raise AwsCorePolicyError("AWS_CAPABILITY_NOT_REGISTERED")
