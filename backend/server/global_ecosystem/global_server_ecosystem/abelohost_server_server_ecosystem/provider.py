"""Abelohost provider adapter binding for GLOBAL SERVER.

This namespace follows the provider/layer package convention used by
API, CORE, ENGINE and DATABASE. It reuses the existing SERVER adapter and
does not claim a live connection or provider-specific service capability.
"""
from ..abelohost_server import AbelohostServerProvider

PROVIDER_ID = "abelohost"
DISPLAY_NAME = "Abelohost"
OWNING_DOMAIN = "SERVER"
ADAPTER_CLASS = AbelohostServerProvider

__all__ = ["PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN", "ADAPTER_CLASS"]
