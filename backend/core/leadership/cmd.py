"""
CORE CMD Role

Defines the Chairman and Managing Director role.

In this architecture, CMD may be held by the same person
who is the Supreme Owner, Founder and CEO.

Technical execution belongs to backend/engines.
"""

from typing import Any, Dict

from .base import LeadershipRole


class CMDRole(LeadershipRole):
    """
    Chairman & Managing Director leadership role.
    """

    def __init__(
        self,
        owner_identity: str = "DR RAJESH KHANDELWAL IBC",
    ) -> None:
        super().__init__(
            role_name="CMD",
            level="executive",
            responsibilities=[
                "Provide overall executive leadership",
                "Guide corporate and business governance",
                "Set major organizational priorities",
                "Coordinate strategic and operational leadership",
                "Review major business decisions",
                "Oversee management performance",
                "Guide long-term organizational development",
                "Coordinate execution of approved strategic objectives",
            ],
            authority=[
                "CHAIRMAN_AUTHORITY",
                "MANAGING_DIRECTOR_AUTHORITY",
                "EXECUTIVE_GOVERNANCE",
                "STRATEGIC_DIRECTION",
                "MANAGEMENT_OVERSIGHT",
                "OPERATIONAL_OVERSIGHT",
                "BUSINESS_GOVERNANCE",
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
        }

    def get_identity(self) -> Dict[str, Any]:
        """Return the CMD identity representation."""
        return dict(self.identity)

    def is_same_as_owner(self) -> bool:
        """Return whether CMD and Supreme Owner are the same person."""
        return True

    def is_same_as_founder(self) -> bool:
        """Return whether CMD and Founder are the same person."""
        return True

    def is_same_as_ceo(self) -> bool:
        """Return whether CMD and CEO are the same person."""
        return True

    def describe(self) -> Dict[str, Any]:
        """Return the complete CMD role description."""
        data = super().describe()
        data.update(
            {
                "owner_identity": self.owner_identity,
                "identity": self.get_identity(),
                "same_as_supreme_owner": self.is_same_as_owner(),
                "same_as_founder": self.is_same_as_founder(),
                "same_as_ceo": self.is_same_as_ceo(),
            }
        )
        return data
