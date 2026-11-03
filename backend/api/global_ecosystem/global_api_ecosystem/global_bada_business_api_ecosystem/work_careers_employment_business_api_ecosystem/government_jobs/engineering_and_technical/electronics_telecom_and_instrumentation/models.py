"""Domain model for Electronics, telecom and instrumentation posts."""
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class GovernmentPost:
    post_id: str
    post_title: str
    recruiting_authority: str
    technical_grade: str
    electronics_telecom_or_instrumentation: str
    network_or_control_site: str
    employment_status: str = "notices_to_be_verified"
    notification_reference: Optional[str] = None
    official_notice_url: Optional[str] = None

    @property
    def work_function(self) -> str:
        return "systems_and_instrumentation"
