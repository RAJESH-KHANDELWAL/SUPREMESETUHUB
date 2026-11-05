"""Global Water Resources & Marine Industries business ecosystem entry point.

The maintained industry implementation remains in
industry_api_ecosystems/water_resources_marine_industries.
This facade exposes it under the Global Bada Business root without
duplicating source files or changing the stable industry/API identifier.
"""
from pathlib import Path as _Path

from ..industry_api_ecosystems.water_resources_marine_industries import *

__path__ = [str(_Path(__file__).resolve().parent.parent / "industry_api_ecosystems" / "water_resources_marine_industries")]
