"""Microsoft Azure provider adapter binding for GLOBAL SERVER.

This namespace mirrors sibling layer package naming and reuses the
existing provider adapter. It does not claim live connectivity.
"""
from ..azure_server_ecosystem import AzureServerEcosystem

PROVIDER_ID = "azure"
DISPLAY_NAME = "Microsoft Azure"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = AzureServerEcosystem

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
