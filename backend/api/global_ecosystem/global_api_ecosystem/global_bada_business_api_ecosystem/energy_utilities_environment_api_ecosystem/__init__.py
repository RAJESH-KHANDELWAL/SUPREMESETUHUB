"""Compatibility entry point for the Energy, Utilities & Environment API Ecosystem."""
from pathlib import Path as _Path
from ..industry_api_ecosystems.energy_utilities_environment import *
__path__ = [str(_Path(__file__).resolve().parent.parent / "industry_api_ecosystems" / "energy_utilities_environment")]
