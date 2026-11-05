"""Unified Global Real Estate, Construction, Infrastructure & Property Business entry point."""
from pathlib import Path as _Path
from ..industry_api_ecosystems.real_estate_construction import *
from ..industry_api_ecosystems.real_estate_construction_infrastructure import *
_BASE = _Path(__file__).resolve().parent
__path__ = [
    str(_BASE),
    str(_BASE.parent / "industry_api_ecosystems" / "real_estate_construction"),
    str(_BASE.parent / "industry_api_ecosystems" / "real_estate_construction_infrastructure"),
]
