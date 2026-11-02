"""
CORE Owner / Supreme Authority

Single ultimate ownership authority for the SupremeSetuHub system.

Multiple identities and official brand representations can belong
to the same Supreme Owner.

This module defines ownership and authority.
Technical execution belongs to backend/engines.
"""

from typing import Any, Dict, List

from .base import LeadershipRole


class OwnerRole(LeadershipRole):
    """
    Supreme Owner / Administrator role.
    """

    def __init__(self) -> None:
        super().__init__(
            role_name="SUPREME_OWNER",
            level="supreme",
            responsibilities=[
                "Own the overall system and business ecosystem",
                "Define overall vision and direction",
                "Approve major strategic decisions",
                "Govern leadership and management",
                "Control ownership-level policies",
                "Oversee server, system, software, web, website and app ecosystem",
                "Assign responsibilities to leadership and management",
            ],
            authority=[
                "SUPREME_OWNERSHIP",
                "SYSTEM_ADMINISTRATION",
                "STRATEGIC_DECISION",
                "LEADERSHIP_ASSIGNMENT",
                "BUSINESS_GOVERNANCE",
                "SYSTEM_GOVERNANCE",
                "PLATFORM_GOVERNANCE",
            ],
        )

        self.identities: List[Dict[str, Any]] = [
            {
                "display_name": "👑 RAJESHKHANDELWAL 👑",
                "username": "rajeshkhandelwal",
                "domain": "rajeshkhandelwal.com",
                "www": "www.rajeshkhandelwal.com",
                "type": "personal",
                "official": False,
            },
            {
                "display_name": "👑 RAJESH KHANDELWAL 👑",
                "username": "rajesh-khandelwal",
                "domain": "rajeshkhandelwal.com",
                "www": "www.rajeshkhandelwal.com",
                "type": "personal",
                "official": False,
            },
            {
                "display_name": "👑 RAJESHKHANDELWALOFFICIAL 👑",
                "username": "rajeshkhandelwalofficial",
                "domain": "rajeshkhandelwalofficial.com",
                "www": "www.rajeshkhandelwalofficial.com",
                "type": "official_identity",
                "official": True,
            },
            {
                "display_name": "👑 RAJESH KHANDELWAL OFFICIAL 👑",
                "username": "rajesh-khandelwal-official",
                "domain": "rajeshkhandelwalofficial.com",
                "www": "www.rajeshkhandelwalofficial.com",
                "type": "official_identity",
                "official": True,
            },
            {
                "display_name": "👑 DRRAJESHKHANDELWALIBC 👑",
                "username": "drrajeshkhandelwalibc",
                "domain": "drrajeshkhandelwalibc.com",
                "www": "www.drrajeshkhandelwalibc.com",
                "type": "brand_identity",
                "official": True,
            },
            {
                "display_name": "👑 DR RAJESH KHANDELWAL IBC 👑",
                "username": "dr-rajesh-khandelwal-ibc",
                "domain": "drrajeshkhandelwalibc.com",
                "www": "www.drrajeshkhandelwalibc.com",
                "type": "brand_identity",
                "official": True,
            },
            {
                "display_name": "👑 DRRAJESHKHANDELWALIBCOFFICIAL 👑",
                "username": "drrajeshkhandelwalibcofficial",
                "domain": "drrajeshkhandelwalibcofficial.com",
                "www": "www.drrajeshkhandelwalibcofficial.com",
                "type": "official_brand_identity",
                "official": True,
            },
            {
                "display_name": "👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑",
                "username": "dr-rajesh-khandelwal-ibc-official",
                "domain": "drrajeshkhandelwalibcofficial.com",
                "www": "www.drrajeshkhandelwalibcofficial.com",
                "type": "official_brand_identity",
                "official": True,
            },
        ]

        self.system_scope: List[str] = [
            "SERVER",
            "SYSTEM",
            "SOFTWARE",
            "WEB",
            "WEBSITE",
            "APP",
        ]

    def list_identities(self) -> List[Dict[str, Any]]:
        """Return all registered owner identity representations."""
        return list(self.identities)

    def is_owner_identity(self, display_name: str) -> bool:
        """Check whether a display name belongs to the registered owner."""
        normalized = display_name.strip().lower()

        return any(
            identity["display_name"].replace("👑", "").strip().lower()
            == normalized.replace("👑", "").strip().lower()
            for identity in self.identities
        )

    def get_identity(self, username: str) -> Dict[str, Any] | None:
        """Find an owner identity by username."""
        normalized = username.strip().lower()

        for identity in self.identities:
            if identity["username"].lower() == normalized:
                return dict(identity)

        return None

    def add_identity(
        self,
        display_name: str,
        username: str,
        domain: str,
        www: str,
        identity_type: str = "identity",
        official: bool = False,
    ) -> None:
        """Register an additional owner identity representation."""

        if not display_name.strip():
            raise ValueError("display_name cannot be empty")

        if not username.strip():
            raise ValueError("username cannot be empty")

        if not domain.strip():
            raise ValueError("domain cannot be empty")

        if not www.strip():
            raise ValueError("www cannot be empty")

        if self.get_identity(username):
            return

        clean_display_name = display_name.strip()

        if not clean_display_name.startswith("👑"):
            clean_display_name = f"👑 {clean_display_name}"

        if not clean_display_name.endswith("👑"):
            clean_display_name = f"{clean_display_name} 👑"

        self.identities.append(
            {
                "display_name": clean_display_name,
                "username": username.strip(),
                "domain": domain.strip(),
                "www": www.strip(),
                "type": identity_type,
                "official": official,
            }
        )

    def get_system_scope(self) -> List[str]:
        """Return the systems governed by the Supreme Owner."""
        return list(self.system_scope)
