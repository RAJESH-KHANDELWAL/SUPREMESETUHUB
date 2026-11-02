"""Root-level compatibility entry point for the energy_utilities_environment industry ecosystem.

The maintained implementation remains in industry_api_ecosystems/energy_utilities_environment.
This facade exposes it at the global_bada_business_api_ecosystem root
without duplicating source files or breaking existing imports.
"""
from pathlib import Path as _Path

from ..industry_api_ecosystems.energy_utilities_environment import *

__path__ = [str(_Path(__file__).resolve().parent.parent / "industry_api_ecosystems" / "energy_utilities_environment")]
