"""LINKSETU verification experience service."""


class LinkSetuVerificationService:
    """Manage verification status in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_statuses = (
        "unverified",
        "pending",
        "verified",
        "rejected",
    )

    def get_verification_status(
        self,
        entity_id: str,
        entity_type: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "entity_id": entity_id,
            "entity_type": entity_type,
            "status": "unverified",
        }

    def submit_verification(
        self,
        entity_id: str,
        entity_type: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "entity_id": entity_id,
            "entity_type": entity_type,
            "status": "pending",
        }

    def set_verification_status(
        self,
        entity_id: str,
        entity_type: str,
        status: str,
    ) -> dict:

        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported verification status: {status}"
            )

        return {
            "platform": self.platform_name,
            "entity_id": entity_id,
            "entity_type": entity_type,
            "status": status,
        }
