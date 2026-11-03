"""Domain model for Software and application development posts."""
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class GovernmentPost:
    post_id: str
    post_title: str
    recruiting_authority: str
    it_grade: str
    digital_department: str
    software_specialism: str
    employment_status: str = "notices_to_be_verified"
    notification_reference: Optional[str] = None
    official_notice_url: Optional[str] = None

    @property
    def work_function(self) -> str:
        return "public_digital_service_development"
