"""MAIN BASE FOUNDATION organization model."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Organization:
    """Represent a registered organization or operational entity."""

    organization_id: str
    organization_name: str
    organization_type: str = "BUSINESS"
    operating_model: str = ""
    country: str = ""
    region: str = ""
    owner_id: Optional[str] = None
    facility_type: Optional[str] = None
    status: str = "ACTIVE"
    verified: bool = False
    enabled: bool = True
    description: Optional[str] = None

    # Contact and display fields used by OrganizationService persistence.
    display_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None

    def to_dict(self) -> dict:
        """Return a JSON-serializable representation."""
        return {
            "organization_id": self.organization_id,
            "organization_name": self.organization_name,
            "display_name": self.display_name or self.organization_name,
            "organization_type": self.organization_type,
            "operating_model": self.operating_model,
            "country": self.country,
            "region": self.region,
            "owner_id": self.owner_id,
            "facility_type": self.facility_type,
            "status": self.status,
            "verified": self.verified,
            "enabled": self.enabled,
            "description": self.description,
            "email": self.email,
            "phone": self.phone,
            "website": self.website,
        }
