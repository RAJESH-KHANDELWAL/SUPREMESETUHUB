"""Backward-compatible facade; canonical security registry lives in manager.py."""
from .manager import (
    get_catalog,
    get_security_core_catalog,
    list_security_core_modules,
)

__all__ = ["get_catalog", "get_security_core_catalog", "list_security_core_modules"]
