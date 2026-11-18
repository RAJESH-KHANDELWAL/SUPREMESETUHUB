"""Typed records for the students_education_skills domain package."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class CategoryRecord:
    id: str
    name: str
    domain_id: str
    adult_restricted: bool = False

