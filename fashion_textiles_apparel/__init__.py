"""Root-level compatibility entry point for the fashion_textiles_apparel industry ecosystem.

The maintained implementation remains in industry_api_ecosystems/fashion_textiles_apparel.
This facade exposes it at the global_bada_business_api_ecosystem root
without duplicating source files or breaking existing imports.
"""
from pathlib import Path as _Path

from ..industry_api_ecosystems.fashion_textiles_apparel import *

__path__ = [str(_Path(__file__).resolve().parent.parent / "industry_api_ecosystems" / "fashion_textiles_apparel")]
