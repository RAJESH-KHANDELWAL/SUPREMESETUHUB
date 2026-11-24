"""ViceTemple provider adapter binding for GLOBAL SERVER.

This namespace mirrors sibling layer package naming and reuses the
existing provider adapter. It does not claim live connectivity.
"""
from ..vicetemple_server_ecosystem import ViceTempleServerEcosystem

PROVIDER_ID = "vicetemple"
DISPLAY_NAME = "ViceTemple"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = ViceTempleServerEcosystem

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
