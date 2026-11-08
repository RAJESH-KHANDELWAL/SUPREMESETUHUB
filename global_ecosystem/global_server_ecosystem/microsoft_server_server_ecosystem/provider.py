"""Microsoft provider adapter binding for GLOBAL SERVER.

This namespace mirrors sibling layer package naming and reuses the
existing provider adapter. It does not claim live connectivity.
"""
from ..microsoft_server_ecosystem import MicrosoftServerEcosystem

PROVIDER_ID = "microsoft"
DISPLAY_NAME = "Microsoft"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = MicrosoftServerEcosystem

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
