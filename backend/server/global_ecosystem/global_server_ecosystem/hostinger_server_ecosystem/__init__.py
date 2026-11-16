"""Hostinger provider package in GLOBAL SERVER ECOSYSTEM."""
from ..hostinger_server import HostingerServerEcosystem

PROVIDER_ID = "hostinger"
DISPLAY_NAME = "Hostinger"
OWNING_DOMAIN = "SERVER"

__all__ = ["HostingerServerEcosystem", "PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN"]
