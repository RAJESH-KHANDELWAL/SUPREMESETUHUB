"""Stable identifiers and policy constants for the Anthropic domain catalog."""
PROVIDER_ID = "anthropic"
PROVIDER_NAME = "Anthropic"
PROVIDER_TYPE = "foundation_model_provider"
CATALOG_VERSION = "1.0.0"
STATUS_CATALOG_ONLY = "CATALOG_ONLY"
STATUS_NOT_CONFIGURED = "NOT_CONFIGURED"
STATUS_READY = "READY"
STATUS_DEGRADED = "DEGRADED"
SUPPORTED_API_HOSTS = ("api.anthropic.com",)
DEFAULT_API_VERSION = "2023-06-01"
SENSITIVE_CAPABILITIES = frozenset({"admin_workspaces", "files", "managed_agents"})
