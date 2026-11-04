"""Root-level compatibility entry point for the digital_infrastructure_telecommunications industry ecosystem.

The maintained implementation remains in industry_api_ecosystems/digital_infrastructure_telecommunications.
This facade exposes it at the global_bada_business_api_ecosystem root
without duplicating source files or breaking existing imports.
"""
from pathlib import Path as _Path

from ..industry_api_ecosystems.digital_infrastructure_telecommunications import *

__path__ = [str(_Path(__file__).resolve().parent.parent / "industry_api_ecosystems" / "digital_infrastructure_telecommunications")]
