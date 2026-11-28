"""Hostinger provider adapter binding for GLOBAL SERVER.

This namespace mirrors sibling layer package naming and reuses the
existing provider adapter. It does not claim live connectivity.
"""
from ..hostinger_server_ecosystem import HostingerServerEcosystem

PROVIDER_ID = "hostinger"
DISPLAY_NAME = "Hostinger"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = HostingerServerEcosystem

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
