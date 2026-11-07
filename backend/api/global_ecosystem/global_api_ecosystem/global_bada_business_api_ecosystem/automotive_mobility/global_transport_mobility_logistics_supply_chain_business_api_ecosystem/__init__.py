"""Unified Global Transport, Mobility, Logistics & Supply Chain Business entry point."""
from pathlib import Path as _Path

# The Transport, Mobility & Logistics industry identity is owned here.
INDUSTRY_ID = "transport_mobility_logistics"
INDUSTRY_NAME = "Transport, Mobility & Logistics"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"

# Preserve the separate Transport, Logistics & Supply Chain API exports.
from ...transport_logistics_supply_chain import *

_BASE = _Path(__file__).resolve().parent
_BADA_ROOT = _BASE.parent.parent
__path__ = [
    str(_BASE),
    str(_BADA_ROOT / "transport_logistics_supply_chain"),
]
