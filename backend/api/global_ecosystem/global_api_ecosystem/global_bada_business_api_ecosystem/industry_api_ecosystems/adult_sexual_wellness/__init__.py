"""Legacy import alias for restricted 18+ taxonomy.

Canonical categories live in personal_lifestyle_wellness and are excluded
from default discovery unless include_adult=true is explicitly supplied.
"""
from ..personal_lifestyle_wellness import *
LEGACY_INDUSTRY_ID="adult_sexual_wellness"
ACCESS_CLASS="18_plus_restricted"
