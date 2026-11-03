"""Typed schema for central ministry/department directory records."""
from typing import TypedDict

class GovernmentDepartmentSchema(TypedDict):
    id: str
    name: str
    department_type: str
    parent_ministry: str
    jurisdiction: str
    official_website: str
    recruiting_authority: str
    employment_domains: list[str]
    source_status: str
