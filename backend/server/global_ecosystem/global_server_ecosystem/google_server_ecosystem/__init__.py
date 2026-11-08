"""Google Cloud provider package in GLOBAL SERVER ECOSYSTEM."""
from ..google_server import GoogleServerEcosystem

PROVIDER_ID = "google"
DISPLAY_NAME = "Google Cloud"
OWNING_DOMAIN = "SERVER"

__all__ = ["GoogleServerEcosystem", "PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN"]
