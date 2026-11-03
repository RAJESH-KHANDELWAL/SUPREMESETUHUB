"""Compatibility facade for the maintained food_hospitality_restaurants package."""
from .industry_api_ecosystems import food_hospitality_restaurants as _implementation

__path__ = _implementation.__path__
