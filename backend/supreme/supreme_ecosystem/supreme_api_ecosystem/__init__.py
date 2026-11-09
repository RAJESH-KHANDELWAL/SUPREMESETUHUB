"""SUPREME ECOSYSTEM API package.

This package owns the HTTP/API boundary only. Domain rules and orchestration
remain in SUPREME ecosystem services/controllers; persistence remains in the
separately owned database layer.
"""
from .contracts import API_NAME, API_VERSION, API_LAYER_BOUNDARIES

__all__ = ["API_NAME", "API_VERSION", "API_LAYER_BOUNDARIES"]
