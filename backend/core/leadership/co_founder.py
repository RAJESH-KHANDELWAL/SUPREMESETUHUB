"""
CORE Co-Founder Role

Defines the Co-Founder leadership role.

A Co-Founder is a separate leadership role from Founder,
but the actual person/identity must be explicitly configured.
This module does not assume or invent a person.
"""

from typing import Any, Dict, Optional

from .base import LeadershipRole


class CoFounderRole(LeadershipRole):
    """
    Co-Founder-level leadership role.
    """

    def __init__(
        self,
        identity: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(
            role_name="CO_FOUNDER",
            level="executive",
            responsibilities=[
                "Support the founding vision",
                "Participate in strategic planning",
                "Support business and organizational development",
                "Lead assigned strategic areas",
                "Coordinate with Founder and executive leadership",
                "Support long-term platform development",
            ],
            authority=[
                "CO_FOUNDING_VISION",
                "STRATEGIC_PLANNING",
                "ASSIGNED_EXECUTIVE_DECISION",
                "BUSINESS_DEVELOPMENT",
                "ORGANIZATION_DEVELOPMENT",
            ],
        )

        self.identity = identity

    def is_configured(self) -> bool:
        """Return whether a Co-Founder identity has been configured."""
        return self.identity is not None

    def get_identity(self) -> Optional[Dict[str, Any]]:
        """Return the configured Co-Founder identity."""
        if self.identity is None:
            return None

        return dict(self.identity)

    def configure_identity(
        self,
        display_name: str,
        username: str,
        domain: str,
        www: str,
    ) -> None:
        """Configure a Co-Founder identity explicitly."""

        if not display_name.strip():
            raise ValueError("display_name cannot be empty")

        if not username.strip():
            raise ValueError("username cannot be empty")

        if not domain.strip():
            raise ValueError("domain cannot be empty")

        if not www.strip():
            raise ValueError("www cannot be empty")

        self.identity = {
            "display_name": display_name.strip(),
            "username": username.strip(),
            "domain": domain.strip(),
            "www": www.strip(),
        }

    def clear_identity(self) -> None:
        """Remove the configured Co-Founder identity."""
        self.identity = None
