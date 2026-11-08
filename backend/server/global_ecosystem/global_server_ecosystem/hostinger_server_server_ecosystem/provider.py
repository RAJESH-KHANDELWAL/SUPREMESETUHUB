"""Hostinger provider adapter binding for GLOBAL SERVER.

This namespace follows the provider/layer package convention used by
API, CORE, ENGINE and DATABASE. It reuses the existing SERVER adapter and
does not claim a live connection or provider-specific service capability.
"""
from ..hostinger_server import HostingerServerEcosystem

PROVIDER_ID = "hostinger"
DISPLAY_NAME = "Hostinger"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = HostingerServerEcosystem

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
