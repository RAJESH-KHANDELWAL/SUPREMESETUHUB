"""
CORE Founder Role

The Founder role represents the founding authority, vision,
mission and long-term direction of the system/business.

The Founder can be the same person as the Supreme Owner.

Technical execution belongs to backend/engines.
"""

from typing import Any, Dict

from .base import LeadershipRole


class FounderRole(LeadershipRole):
    """
    Founder-level leadership role.

    In this architecture, the Founder may be the same person
    who holds Supreme Owner authority.
    """

    def __init__(
        self,
        owner_identity: str = "DR RAJESH KHANDELWAL IBC",
    ) -> None:
        super().__init__(
            role_name="FOUNDER",
            level="executive",
            responsibilities=[
                "Define the founding vision",
                "Define the mission and long-term direction",
                "Establish core business principles",
                "Shape products, services and platforms",
                "Set long-term strategic priorities",
                "Build and develop the organization",
                "Guide leadership and management",
                "Protect the founding principles of the ecosystem",
            ],
            authority=[
                "FOUNDING_VISION",
                "MISSION_DIRECTION",
                "STRATEGIC_PLANNING",
                "PRODUCT_DIRECTION",
                "BUSINESS_DIRECTION",
                "ORGANIZATION_DIRECTION",
                "FOUNDATION_GOVERNANCE",
            ],
        )

        # Founder and Supreme Owner may represent the same person.
        self.owner_identity = owner_identity

        self.identity: Dict[str, Any] = {
            "display_name": "👑 DR RAJESH KHANDELWAL IBC 👑",
            "username": "drrajeshkhandelwalibc",
            "domain": "drrajeshkhandelwalibc.com",
            "www": "www.drrajeshkhandelwalibc.com",
            "same_as_supreme_owner": True,
        }

    def get_identity(self) -> Dict[str, Any]:
        """Return the Founder identity representation."""
        return dict(self.identity)

    def is_same_as_owner(self) -> bool:
        """Return whether Founder and Supreme Owner are the same authority."""
        return True

    def describe(self) -> Dict[str, Any]:
        """Return the complete Founder role description."""
        data = super().describe()
        data.update(
            {
                "owner_identity": self.owner_identity,
                "identity": self.get_identity(),
                "same_as_supreme_owner": self.is_same_as_owner(),
            }
        )
        return data
