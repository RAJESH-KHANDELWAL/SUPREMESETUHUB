"""
CORE MD Role

Defines the Managing Director role.

In this architecture, MD may be held by the same person
who is the Supreme Owner, Founder, CEO and CMD.

Technical execution belongs to backend/engines.
"""

from typing import Any, Dict

from .base import LeadershipRole


class MDRole(LeadershipRole):
    """
    Managing Director leadership role.
    """

    def __init__(
        self,
        owner_identity: str = "DR RAJESH KHANDELWAL IBC",
    ) -> None:
        super().__init__(
            role_name="MD",
            level="executive",
            responsibilities=[
                "Lead business and organizational operations",
                "Convert strategic direction into operating plans",
                "Coordinate departments and management",
                "Monitor execution and operational performance",
                "Manage business priorities",
                "Coordinate resources and responsibilities",
                "Review operational workflows",
                "Support organizational growth and development",
            ],
            authority=[
                "MANAGING_DIRECTOR_AUTHORITY",
                "OPERATIONAL_DIRECTION",
                "BUSINESS_OPERATIONS",
                "MANAGEMENT_COORDINATION",
                "RESOURCE_COORDINATION",
                "WORKFLOW_OVERSIGHT",
                "PERFORMANCE_OVERSIGHT",
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
        }

    def get_identity(self) -> Dict[str, Any]:
        """Return the MD identity representation."""
        return dict(self.identity)

    def is_same_as_owner(self) -> bool:
        """Return whether MD and Supreme Owner are the same person."""
        return True

    def is_same_as_founder(self) -> bool:
        """Return whether MD and Founder are the same person."""
        return True

    def is_same_as_ceo(self) -> bool:
        """Return whether MD and CEO are the same person."""
        return True

    def is_same_as_cmd(self) -> bool:
        """Return whether MD and CMD are the same person."""
        return True

    def describe(self) -> Dict[str, Any]:
        """Return the complete MD role description."""
        data = super().describe()
        data.update(
            {
                "owner_identity": self.owner_identity,
                "identity": self.get_identity(),
                "same_as_supreme_owner": self.is_same_as_owner(),
                "same_as_founder": self.is_same_as_founder(),
                "same_as_ceo": self.is_same_as_ceo(),
                "same_as_cmd": self.is_same_as_cmd(),
            }
        )
        return data
