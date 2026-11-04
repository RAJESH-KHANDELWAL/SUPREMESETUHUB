"""Compatibility alias for the consolidated Global Agriculture ecosystem package.

The maintained implementation lives under global_agriculture_food_natural_resources_api_ecosystem.
"""
from pathlib import Path as _Path
from ...global_agriculture_food_natural_resources_api_ecosystem.industry_api_ecosystems.agriculture_food_natural_resources import *

__path__ = [str(_Path(__file__).resolve().parents[2] / "global_agriculture_food_natural_resources_api_ecosystem" / "industry_api_ecosystems" / "agriculture_food_natural_resources")]
