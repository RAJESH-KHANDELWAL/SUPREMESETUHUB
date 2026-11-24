"""Abelohost provider package in GLOBAL SERVER ECOSYSTEM."""
from ..abelohost_server import AbelohostServerEcosystem

PROVIDER_ID = "abelohost"
DISPLAY_NAME = "Abelohost"
OWNING_DOMAIN = "SERVER"

__all__ = ["AbelohostServerEcosystem", "PROVIDER_ID", "DISPLAY_NAME", "OWNING_DOMAIN"]
