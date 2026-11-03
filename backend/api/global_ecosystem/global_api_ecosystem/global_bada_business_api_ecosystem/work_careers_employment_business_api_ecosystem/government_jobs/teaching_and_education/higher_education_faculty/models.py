"""Domain model for College and university faculty posts."""
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class GovernmentPost:
    post_id: str
    post_title: str
    recruiting_authority: str
    faculty_rank: str
    institution_type: str
    academic_discipline: str
    employment_status: str = "notices_to_be_verified"
    notification_reference: Optional[str] = None
    official_notice_url: Optional[str] = None

    @property
    def work_function(self) -> str:
        return "higher_education_and_research"
