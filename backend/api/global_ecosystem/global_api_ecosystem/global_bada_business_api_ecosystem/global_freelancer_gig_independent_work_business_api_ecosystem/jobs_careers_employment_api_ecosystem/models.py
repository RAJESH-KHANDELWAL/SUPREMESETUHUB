"""Typed category records for the Work, Jobs & Careers taxonomy."""
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True, slots=True)
class CategoryRecord:
    id: str
    name: str
    domain_id: str
    adult_restricted: bool = False
    description: str = ""
    category_type: str = "unspecified"
    ownership_sectors: Tuple[str, ...] = ()
    employer_organization_types: Tuple[str, ...] = ()
    employment_types: Tuple[str, ...] = ()
    work_arrangements: Tuple[str, ...] = ()
    seniority_levels: Tuple[str, ...] = ()
    audience_groups: Tuple[str, ...] = ()
    search_terms: Tuple[str, ...] = ()
    scope_notes: Tuple[str, ...] = ()
    verification_requirements: Tuple[str, ...] = ()
    related_category_ids: Tuple[str, ...] = ()
    taxonomy_status: str = "taxonomy_only"
