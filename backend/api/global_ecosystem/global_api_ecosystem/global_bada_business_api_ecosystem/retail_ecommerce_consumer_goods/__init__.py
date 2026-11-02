"""Root-level compatibility entry point for the retail_ecommerce_consumer_goods industry ecosystem.

The maintained implementation remains in industry_api_ecosystems/retail_ecommerce_consumer_goods.
This facade exposes it at the global_bada_business_api_ecosystem root
without duplicating source files or breaking existing imports.
"""
from pathlib import Path as _Path

from ..industry_api_ecosystems.retail_ecommerce_consumer_goods import *

__path__ = [str(_Path(__file__).resolve().parent.parent / "industry_api_ecosystems" / "retail_ecommerce_consumer_goods")]
