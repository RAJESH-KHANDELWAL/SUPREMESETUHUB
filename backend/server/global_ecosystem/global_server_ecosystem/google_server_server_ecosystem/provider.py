"""Google Cloud provider adapter binding for GLOBAL SERVER.

This namespace mirrors sibling layer package naming and reuses the
existing provider adapter. It does not claim live connectivity.
"""
from ..google_server_ecosystem import GoogleServerEcosystem

PROVIDER_ID = "google"
DISPLAY_NAME = "Google Cloud"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = GoogleServerEcosystem

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
