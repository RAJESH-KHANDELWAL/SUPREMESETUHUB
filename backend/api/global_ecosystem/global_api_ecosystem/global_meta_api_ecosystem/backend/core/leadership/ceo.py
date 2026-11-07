"""
CORE CEO Role

Defines the Chief Executive Officer role.

In this architecture, the CEO may be the same person as the
Supreme Owner and Founder.

Technical execution belongs to backend/engines.
"""

from typing import Any, Dict

from .base import LeadershipRole


class CEORole(LeadershipRole):
    """
    CEO-level executive leadership role.

    The CEO is responsible for overall execution,
    management and operational direction.
    """

    def __init__(
        self,
        owner_identity: str = "DR RAJESH KHANDELWAL IBC",
    ) -> None:
        super().__init__(
            role_name="CEO",
            level="executive",
            responsibilities=[
                "Lead overall business execution",
                "Convert strategy into operational plans",
                "Coordinate management and leadership",
                "Set organizational priorities",
                "Monitor business performance",
                "Coordinate teams and departments",
                "Approve operational workflows",
                "Drive execution of approved business objectives",
            ],
            authority=[
                "EXECUTIVE_DECISION",
                "OPERATIONAL_DIRECTION",
                "MANAGEMENT_COORDINATION",
                "TEAM_COORDINATION",
                "WORKFLOW_APPROVAL",
                "BUSINESS_EXECUTION",
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
        }

    def get_identity(self) -> Dict[str, Any]:
        """Return the CEO identity representation."""
        return dict(self.identity)

    def is_same_as_owner(self) -> bool:
        """Return whether CEO and Supreme Owner are the same person."""
        return True

    def is_same_as_founder(self) -> bool:
        """Return whether CEO and Founder are the same person."""
        return True

    def describe(self) -> Dict[str, Any]:
        """Return the complete CEO role description."""
        data = super().describe()
        data.update(
            {
                "owner_identity": self.owner_identity,
                "identity": self.get_identity(),
                "same_as_supreme_owner": self.is_same_as_owner(),
                "same_as_founder": self.is_same_as_founder(),
            }
        )
        return data
