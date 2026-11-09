"""Compatibility exports for the adult sexual wellness taxonomy.

The maintained taxonomy lives under industry_api_ecosystems.personal_lifestyle_wellness.
This compatibility module keeps the legacy adult industry identifiers available
without retaining a duplicate adult_sexual_wellness package directory.
"""
from ..personal_lifestyle_wellness import *

LEGACY_INDUSTRY_ID = "adult_sexual_wellness"
ACCESS_CLASS = "18_plus_restricted"
