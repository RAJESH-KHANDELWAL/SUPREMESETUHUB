"""DOMAIN CORE ECOSYSTEM package.

This package is an independent layer-owned namespace. It contains no imports
from API, CORE, or ENGINE sibling layers.
"""
LAYER = "CORE"
CATEGORY = "DOMAIN"
ECOSYSTEM_NAME = f"GLOBAL {CATEGORY.replace('_', ' ')} {LAYER} ECOSYSTEM"
ECOSYSTEM_ID = f"GLOBAL-{CATEGORY.replace('_', '-')}-{LAYER.upper()}-ECOSYSTEM"

__all__ = ["LAYER", "CATEGORY", "ECOSYSTEM_NAME", "ECOSYSTEM_ID"]
