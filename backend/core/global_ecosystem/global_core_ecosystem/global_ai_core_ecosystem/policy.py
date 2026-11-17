"""Global AI Core metadata policy; API authorization remains external."""
from collections.abc import Mapping

SENSITIVE = (
    "ADMIN", "DELETE", "WRITE", "PUBLISH", "BILLING", "TRAIN",
    "FINE_TUNE", "UPLOAD", "TOOL", "EXECUTE", "SEND",
)
_SECRET_KEYS = {
    "token", "access_token", "refresh_token", "client_secret", "api_key",
    "secret", "authorization", "password", "credential_value", "private_key",
}


class GlobalAICorePolicyError(PermissionError):
    pass


class GlobalAICorePolicy:
    @staticmethod
    def require_tenant_context(context):
        if context is None or not callable(getattr(context, "validate", None)):
            raise GlobalAICorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        context.validate()

    @staticmethod
    def validate_capability(provider, capability):
        if provider.get("disabled") is True:
            raise GlobalAICorePolicyError("PROVIDER_DISABLED")
        allowed = set(provider.get("capabilities", []))
        if allowed and capability not in allowed:
            raise GlobalAICorePolicyError("CAPABILITY_NOT_REGISTERED")

    @staticmethod
    def classify_capability(capability):
        value = str(capability).upper()
        return (
            "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION_AND_AUDIT"
            if any(item in value for item in SENSITIVE)
            else "STANDARD_REQUIRES_TENANT_AND_PROVIDER_AUTHORIZATION"
        )

    @staticmethod
    def safe_provider_summary(provider):
        """Return a recursively sanitized copy; never mutate registry metadata."""
        def sanitize(value):
            if isinstance(value, Mapping):
                return {
                    key: sanitize(item)
                    for key, item in value.items()
                    if str(key).casefold().replace("-", "_") not in _SECRET_KEYS
                }
            if isinstance(value, tuple):
                return [sanitize(item) for item in value]
            if isinstance(value, list):
                return [sanitize(item) for item in value]
            return value

        return sanitize(provider)
