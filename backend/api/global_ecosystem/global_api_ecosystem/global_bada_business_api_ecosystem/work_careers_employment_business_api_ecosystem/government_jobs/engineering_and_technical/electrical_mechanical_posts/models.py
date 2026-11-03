"""Domain model for Electrical and mechanical engineering posts."""
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class GovernmentPost:
    post_id: str
    post_title: str
    recruiting_authority: str
    engineering_grade: str
    electrical_or_mechanical_discipline: str
    plant_or_utility: str
    employment_status: str = "notices_to_be_verified"
    notification_reference: Optional[str] = None
    official_notice_url: Optional[str] = None

    @property
    def work_function(self) -> str:
        return "equipment_and_plant_operations"
