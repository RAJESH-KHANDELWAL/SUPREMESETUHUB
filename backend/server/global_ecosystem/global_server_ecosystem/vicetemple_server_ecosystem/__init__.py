"""ViceTemple provider package in GLOBAL SERVER ECOSYSTEM."""
from ..vicetemple_server import ViceTempleServerEcosystem

PROVIDER_ID = "vicetemple"
DISPLAY_NAME = "ViceTemple"
OWNING_DOMAIN = "SERVER"

__all__ = ["ViceTempleServerEcosystem", "PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN"]
