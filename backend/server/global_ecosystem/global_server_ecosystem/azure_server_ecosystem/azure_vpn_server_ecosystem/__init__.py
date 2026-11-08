"""VPN SERVER namespace for Microsoft Azure (additional integration); catalog-only until explicitly implemented."""

PROVIDER_ID = "azure"
SERVICE_TYPE_ID = "vpn-server"
DISPLAY_NAME = "VPN SERVER"
OWNING_DOMAIN = "SERVER"
EXECUTION_MODE = "EXPLICIT_ADAPTER_REQUIRED"

__all__ = ["PROVIDER_ID", "SERVICE_TYPE_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "EXECUTION_MODE"]
