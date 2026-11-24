"""Abelohost provider adapter binding for GLOBAL SERVER.

This namespace mirrors sibling layer package naming and reuses the
existing provider adapter. It does not claim live connectivity.
"""
from ..abelohost_server_ecosystem import AbelohostServerEcosystem

PROVIDER_ID = "abelohost"
DISPLAY_NAME = "Abelohost"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = AbelohostServerEcosystem

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
