"""DigitalOcean provider package in GLOBAL SERVER ECOSYSTEM."""
from ..digitalocean_server import DigitalOceanServerEcosystem

PROVIDER_ID = "digitalocean"
DISPLAY_NAME = "DigitalOcean"
OWNING_DOMAIN = "SERVER"

__all__ = ["DigitalOceanServerEcosystem", "PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN"]
