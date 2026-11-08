"""WEB SERVER namespace for Amazon Web Services; catalog-only until explicitly implemented."""

PROVIDER_ID = "aws"
SERVICE_TYPE_ID = "web-server"
DISPLAY_NAME = "WEB SERVER"
OWNING_DOMAIN = "SERVER"
EXECUTION_MODE = "EXPLICIT_ADAPTER_REQUIRED"

__all__ = ["PROVIDER_ID", "SERVICE_TYPE_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "EXECUTION_MODE"]
