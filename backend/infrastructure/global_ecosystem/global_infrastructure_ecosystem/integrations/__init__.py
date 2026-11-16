"""Cross-layer integration adapters for Global Infrastructure.

The catalog is exposed from this package so imports resolve consistently even
though a legacy sibling integrations.py module is retained for compatibility.
"""
from .catalog import INTEGRATIONS

__all__ = ["INTEGRATIONS"]
