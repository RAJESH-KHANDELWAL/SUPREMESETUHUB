"""Root-level compatibility entry point for the government_public_services_social_impact industry ecosystem.

The maintained implementation remains in industry_api_ecosystems/government_public_services_social_impact.
This facade exposes it at the global_bada_business_api_ecosystem root
without duplicating source files or breaking existing imports.
"""
from pathlib import Path as _Path

from ..industry_api_ecosystems.government_public_services_social_impact import *

__path__ = [str(_Path(__file__).resolve().parent.parent / "industry_api_ecosystems" / "government_public_services_social_impact")]
