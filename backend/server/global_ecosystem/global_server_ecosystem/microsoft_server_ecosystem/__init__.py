"""Microsoft Azure provider package in GLOBAL SERVER ECOSYSTEM."""
from ..microsoft_server import MicrosoftServerEcosystem

PROVIDER_ID = "microsoft"
DISPLAY_NAME = "Microsoft Azure"
OWNING_DOMAIN = "SERVER"

__all__ = ["MicrosoftServerEcosystem", "PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN"]
