"""Compatibility entry point for the canonical Fashion, Textiles & Apparel ecosystem.

The maintained implementation lives in global_fashion_textiles_apparel_api_ecosystem.
This facade preserves legacy imports without maintaining duplicate source files.
"""
from pathlib import Path as _Path
from ..global_fashion_textiles_apparel_api_ecosystem import *

__path__ = [str(_Path(__file__).resolve().parent.parent / "global_fashion_textiles_apparel_api_ecosystem")]
