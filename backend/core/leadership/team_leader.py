"""
CORE Team Leader Role

Defines the Team Leader role within the CORE leadership layer.

A Team Leader coordinates a specific team and its assigned work.
Technical execution belongs to backend/engines.
"""

from typing import Any, Dict

from .base import LeadershipRole


class TeamLeaderRole(LeadershipRole):
    """
    Team Leader role.
    """

    def __init__(
        self,
        owner_identity: str = "DR RAJESH KHANDELWAL IBC",
    ) -> None:
        super().__init__(
            role_name="TEAM_LEADER",
            level="team_leadership",
            responsibilities=[
                "Lead an assigned team",
                "Distribute approved tasks within the team",
                "Coordinate daily team work",
                "Support team members",
                "Monitor assigned task progress",
                "Identify and escalate team-level issues",
                "Maintain team communication",
                "Report team status to the Manager or Leader",
                "Support completion of assigned workflows",
            ],
            authority=[
                "TEAM_COORDINATION",
                "TASK_DISTRIBUTION",
                "TEAM_GUIDANCE",
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
            "same_as_leader": True,
        }

    def get_identity(self) -> Dict[str, Any]:
        """Return the configured Team Leader identity."""
        return dict(self.identity)

    def is_same_as_owner(self) -> bool:
        """Return whether Team Leader and Supreme Owner are the same person."""
        return True

    def describe(self) -> Dict[str, Any]:
        """Return the complete Team Leader role description."""
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
                "same_as_leader": self.identity["same_as_leader"],
            }
        )
        return data
