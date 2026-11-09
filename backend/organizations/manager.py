"""MAIN BASE FOUNDATION organization manager."""

from typing import Dict

from .model import Organization


class OrganizationManager:
    """Manage registered organizations and operational entities."""

    def __init__(self):
        self.organizations: Dict[str, Organization] = {}

    def create(
        self,
        organization_id: str,
        organization_name: str,
        organization_type: str,
        operating_model: str,
        country: str,
        region: str,
        owner_id: str | None = None,
        facility_type: str | None = None,
        description: str | None = None,
    ) -> dict:
        """Create an organization after validating its unique identifier."""
        if not organization_id or not organization_id.strip():
            return {"success": False, "error": "ORGANIZATION_ID_REQUIRED"}
        if organization_id in self.organizations:
            return {
                "success": False,
                "error": "ORGANIZATION_ID_ALREADY_EXISTS",
                "organization_id": organization_id,
            }

        organization = Organization(
            organization_id=organization_id,
            organization_name=organization_name,
            organization_type=organization_type,
            operating_model=operating_model,
            country=country,
            region=region,
            owner_id=owner_id,
            facility_type=facility_type,
            description=description,
        )
        self.organizations[organization_id] = organization
        return {"success": True, "organization": organization.__dict__}

    def get(self, organization_id: str) -> dict:
        """Return one organization by ID."""
        organization = self.organizations.get(organization_id)
        if organization is None:
            return {
                "success": False,
                "error": "ORGANIZATION_NOT_FOUND",
                "organization_id": organization_id,
            }
        return {"success": True, "organization": organization.__dict__}

    def list(self, owner_id: str | None = None) -> dict:
        """List organizations, optionally scoped to an owner."""
        organizations = list(self.organizations.values())
        if owner_id is not None:
            organizations = [
                item for item in organizations if item.owner_id == owner_id
            ]
        return {
            "success": True,
            "count": len(organizations),
            "organizations": [item.__dict__ for item in organizations],
        }

    def disable(self, organization_id: str) -> dict:
        """Disable an organization without deleting its record."""
        organization = self.organizations.get(organization_id)
        if organization is None:
            return {"success": False, "error": "ORGANIZATION_NOT_FOUND"}
        organization.enabled = False
        organization.status = "DISABLED"
        return {"success": True, "organization": organization.__dict__}

    def health(self) -> dict:
        """Summarize in-memory organization manager health."""
        active = sum(
            1 for item in self.organizations.values()
            if item.status == "ACTIVE" and item.enabled
        )
        return {
            "system": "Organization Manager",
            "health": "HEALTHY",
            "registered_organizations": len(self.organizations),
            "active_organizations": active,
        }
