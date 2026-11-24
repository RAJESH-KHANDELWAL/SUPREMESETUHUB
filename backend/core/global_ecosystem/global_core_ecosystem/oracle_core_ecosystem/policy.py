"""Core scope and metadata security policy."""
_FORBIDDEN = {"credential_storage", "oauth_token_exchange", "provider_api_transport",
              "database_mutations", "job_execution", "billing_execution", "resource_provisioning"}

def classify_capability(capability: str) -> dict:
    key = capability.strip().lower()
    blocked = key in _FORBIDDEN
    return {"capability": key, "allowed_in_core": not blocked,
            "owner": "dedicated_layer" if blocked else "core_metadata",
            "requires_authenticated_tenant": True}

def redact_sensitive_metadata(value: dict) -> dict:
    secrets = {"token", "access_token", "refresh_token", "client_secret", "private_key", "password"}
    return {key: ("[REDACTED]" if key.lower() in secrets else item) for key, item in value.items()}
