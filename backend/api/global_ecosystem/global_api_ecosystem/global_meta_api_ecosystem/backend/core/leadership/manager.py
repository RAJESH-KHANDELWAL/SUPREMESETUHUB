"""
CORE Manager Role

Defines the Manager leadership role.

Managers coordinate assigned business areas, teams,
workflows and execution.

Technical execution belongs to backend/engines.
"""

from typing import Any, Dict

from .base import LeadershipRole


class ManagerRole(LeadershipRole):
    """
    Manager-level leadership role.
    """

    def __init__(
        self,
        owner_identity: str = "DR RAJESH KHANDELWAL IBC",
    ) -> None:
        super().__init__(
            role_name="MANAGER",
            level="management",
            responsibilities=[
                "Manage assigned business areas",
                "Plan and coordinate assigned work",
                "Assign tasks to team members",
                "Monitor task and workflow progress",
                "Coordinate with team leaders",
                "Report operational status to executive leadership",
                "Identify execution issues",
                "Escalate important decisions to higher authority",
                "Ensure approved workflows are followed",
            ],
            authority=[
                "TEAM_ASSIGNMENT",
                "TASK_ASSIGNMENT",
                "WORKFLOW_COORDINATION",
                "OPERATIONAL_MONITORING",
                "TEAM_COORDINATION",
                "STATUS_REPORTING",
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
        }

    def get_identity(self) -> Dict[str, Any]:
        """Return the configured Manager identity."""
        return dict(self.identity)

    def is_same_as_owner(self) -> bool:
        """Return whether Manager and Supreme Owner are the same person."""
        return True

    def describe(self) -> Dict[str, Any]:
        """Return the complete Manager role description."""
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
            }
        )
        return data
