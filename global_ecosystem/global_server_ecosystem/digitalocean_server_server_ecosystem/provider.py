"""DigitalOcean provider adapter binding for GLOBAL SERVER.

This namespace mirrors sibling layer package naming and reuses the
existing provider adapter. It does not claim live connectivity.
"""
from ..digitalocean_server_ecosystem import DigitalOceanServerEcosystem

PROVIDER_ID = "digitalocean"
DISPLAY_NAME = "DigitalOcean"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = DigitalOceanServerEcosystem

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
