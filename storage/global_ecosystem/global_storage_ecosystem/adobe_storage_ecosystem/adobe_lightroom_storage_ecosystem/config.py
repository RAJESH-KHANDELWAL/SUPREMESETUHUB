"""Compatibility export; canonical configuration lives in ecosystem_config.py."""
from .ecosystem_config import get_config, ECOSYSTEM_ID
__all__ = ["get_config", "ECOSYSTEM_ID"]
