"""EDGE SERVER namespace for Cloudflare; catalog-only until explicitly implemented."""

PROVIDER_ID = "cloudflare"
SERVICE_TYPE_ID = "edge-server"
DISPLAY_NAME = "EDGE SERVER"
OWNING_DOMAIN = "SERVER"
EXECUTION_MODE = "EXPLICIT_ADAPTER_REQUIRED"

__all__ = ["PROVIDER_ID", "SERVICE_TYPE_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "EXECUTION_MODE"]
