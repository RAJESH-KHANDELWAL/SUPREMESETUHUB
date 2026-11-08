"""DigitalOcean provider adapter binding for GLOBAL SERVER.

This namespace follows the provider/layer package convention used by
API, CORE, ENGINE and DATABASE. It reuses the existing SERVER adapter and
does not claim a live connection or provider-specific service capability.
"""
from ..digitalocean_server import DigitalOceanServerEcosystem

PROVIDER_ID = "digitalocean"
DISPLAY_NAME = "DigitalOcean"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = DigitalOceanServerEcosystem

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
