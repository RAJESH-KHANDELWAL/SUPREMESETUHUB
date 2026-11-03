"""API schema for recruitment authority records."""
from typing import Literal, TypedDict

class RecruitmentAuthoritySchema(TypedDict):
    id: str
    name: str
    authority_type: Literal["ministry", "department", "constitutional_body", "statutory_body", "recruiting_commission", "public_institution"]
    jurisdiction: str
    official_website: str
    recruitment_scope: list[str]
    source_status: str
