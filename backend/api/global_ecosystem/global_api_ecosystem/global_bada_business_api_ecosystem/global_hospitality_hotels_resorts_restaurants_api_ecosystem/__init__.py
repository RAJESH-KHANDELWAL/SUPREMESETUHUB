"""Canonical Global Hotels, Resorts, Restaurants & Hospitality ecosystem facade."""
from pathlib import Path as _Path
from ..industry_api_ecosystems import food_hospitality_restaurants as _implementation
from ..industry_api_ecosystems.food_hospitality_restaurants import *

__path__ = _implementation.__path__
