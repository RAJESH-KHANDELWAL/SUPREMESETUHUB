"""Domain model for Veterinary, fisheries and rural development posts."""
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class GovernmentPost:
    post_id: str
    post_title: str
    recruiting_authority: str
    rural_service_grade: str
    rural_or_animal_husbandry_unit: str
    field_programme: str
    employment_status: str = "notices_to_be_verified"
    notification_reference: Optional[str] = None
    official_notice_url: Optional[str] = None

    @property
    def work_function(self) -> str:
        return "rural_and_livelihood_services"
