"""Typed subcategory record for IT & Digital Technology."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Subcategory:
    id: str
    name: str
    description: str
    parent_field_id: str = "it_technology"
