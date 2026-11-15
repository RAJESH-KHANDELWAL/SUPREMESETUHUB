"""Typed record for one Jobs & Careers industry subcategory."""
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class IndustrySubcategoryRecord:
    id: str
    name: str
    category_id: str
    taxonomy_status: str = "taxonomy_scaffold"
