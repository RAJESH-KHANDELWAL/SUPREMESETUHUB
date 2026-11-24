"""Typed Anthropic Core product descriptor."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ProductDescriptor:
    product_id: str
    name: str
    category: str
    api_surface: str | None
    availability: str
