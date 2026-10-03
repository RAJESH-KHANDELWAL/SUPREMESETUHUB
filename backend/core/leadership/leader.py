"""
CORE Leader Role

Defines the general leadership role within the CORE layer.

A Leader guides an assigned area, people, project or workflow.
Technical execution belongs to backend/engines.
"""

from typing import Any, Dict

from .base import LeadershipRole


class LeaderRole(LeadershipRole):
    """
    General leadership role.
    """

    def __init__(
        self,
        owner_identity: str = "DR RAJESH KHANDELWAL IBC",
    ) -> None:
        super().__init__(
            role_name="LEADER",
            level="leadership",
            responsibilities=[
                "Lead assigned teams or business areas",
                "Guide team members toward approved objectives",
                "Coordinate assigned work",
                "Monitor progress and performance",
                "Support team problem solving",
                "Communicate priorities clearly",
                "Report important issues to management",
                "Support successful completion of assigned workflows",
            ],
            authority=[
                "TEAM_LEADERSHIP",
                "WORK_COORDINATION",
                "TASK_GUIDANCE",
                "PROGRESS_MONITORING",
                "TEAM_COMMUNICATION",
                "ISSUE_ESCALATION",
            ],
        )

        self.owner_identity = owner_identity

        self.identity: Dict[str, Any] = {
            "display_name": "👑 DR RAJESH KHANDELWAL IBC 👑",
            "username": "drrajeshkhandelwalibc",
            "domain": "drrajeshkhandelwalibc.com",
            "www": "www.drrajeshkhandelwalibc.com",
            "same_as_supreme_owner": True,
            "same_as_founder": True,
            "same_as_ceo": True,
            "same_as_cmd": True,
            "same_as_md": True,
            "same_as_manager": True,
        }

    def get_identity(self) -> Dict[str, Any]:
        """Return the configured Leader identity."""
        return dict(self.identity)

    def is_same_as_owner(self) -> bool:
        """Return whether Leader and Supreme Owner are the same person."""
        return True

    def describe(self) -> Dict[str, Any]:
        """Return the complete Leader role description."""
        data = super().describe()
        data.update(
            {
                "owner_identity": self.owner_identity,
                "identity": self.get_identity(),
                "same_as_supreme_owner": self.is_same_as_owner(),
                "same_as_founder": self.identity["same_as_founder"],
                "same_as_ceo": self.identity["same_as_ceo"],
                "same_as_cmd": self.identity["same_as_cmd"],
                "same_as_md": self.identity["same_as_md"],
                "same_as_manager": self.identity["same_as_manager"],
            }
        )
        return data
