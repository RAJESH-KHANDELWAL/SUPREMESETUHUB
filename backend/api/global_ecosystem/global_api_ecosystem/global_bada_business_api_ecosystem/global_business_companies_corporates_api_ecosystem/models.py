"""Stable category record contract for the business-company taxonomy."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class CategoryRecord:
    id: str
    name: str
    domain_id: str = "business_companies_corporates"
