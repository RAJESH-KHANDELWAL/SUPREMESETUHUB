"""ViceTemple provider adapter binding for GLOBAL SERVER.

This namespace follows the provider/layer package convention used by
API, CORE, ENGINE and DATABASE. It reuses the existing SERVER adapter and
does not claim a live connection or provider-specific service capability.
"""
from ..vicetemple_server import ViceTempleServerProvider

PROVIDER_ID = "vicetemple"
DISPLAY_NAME = "ViceTemple"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = ViceTempleServerProvider

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
