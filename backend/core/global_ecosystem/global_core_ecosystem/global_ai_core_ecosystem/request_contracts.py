"""Provider-neutral AI task validation."""
from collections.abc import Mapping

_SECRET_KEYS = {
    "token", "access_token", "refresh_token", "authorization", "api_key",
    "client_secret", "private_key", "secret", "password", "credential_value",
}
_ALLOWED_FIELDS = {
    "provider_id", "capability", "model_id", "task", "context",
    "request_id", "options", "metadata",
}
_REQUIRED_FIELDS = {"provider_id", "task"}


def _normalized_key(value):
    return str(value).casefold().replace("-", "_")


def _reject_secret_material(value):
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if _normalized_key(key) in _SECRET_KEYS:
                raise ValueError("SECRET_MATERIAL_FORBIDDEN_IN_CORE")
            _reject_secret_material(nested)
    elif isinstance(value, (list, tuple)):
        for nested in value:
            _reject_secret_material(nested)


def validate_ai_request(payload):
    if not isinstance(payload, Mapping):
        raise ValueError("AI_REQUEST_MUST_BE_A_MAPPING")
    _reject_secret_material(payload)

    missing = _REQUIRED_FIELDS.difference(payload)
    if missing:
        raise ValueError(
            "AI_REQUEST_REQUIRED_FIELDS_MISSING: " + ", ".join(sorted(missing))
        )

    unknown = set(payload).difference(_ALLOWED_FIELDS)
    if unknown:
        raise ValueError(
            "UNSUPPORTED_AI_REQUEST_FIELDS: " + ", ".join(sorted(map(str, unknown)))
        )

    for key in ("provider_id", "capability", "model_id", "task", "request_id"):
        if key in payload and payload[key] is not None:
            if not isinstance(payload[key], str) or not payload[key].strip():
                raise ValueError(key.upper() + "_MUST_BE_NON_EMPTY_STRING")

    if len(payload["task"]) > 12000:
        raise ValueError("AI_TASK_TOO_LONG")

    for key in ("context", "options", "metadata"):
        if key in payload and not isinstance(payload[key], Mapping):
            raise ValueError(key.upper() + "_MUST_BE_A_MAPPING")

    return {
        "accepted": True,
        "execution_performed": False,
        "provider_authorization_verified": False,
    }
