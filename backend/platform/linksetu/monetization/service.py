"""LINKSETU monetization experience service."""


class LinkSetuMonetizationService:
    """Manage monetization experience in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_types = (
        "subscription",
        "promotion",
        "advertising",
        "digital_product",
        "service",
    )

    def create_monetization(
        self,
        owner_id: str,
        entity_id: str,
        monetization_type: str,
    ) -> dict:

        if monetization_type not in self.allowed_types:
            raise ValueError(
                f"Unsupported monetization type: {monetization_type}"
            )

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "entity_id": entity_id,
            "monetization_type": monetization_type,
            "status": "created",
        }

    def get_monetization(
        self,
        entity_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "entity_id": entity_id,
            "monetization": {},
        }

    def get_revenue_summary(
        self,
        owner_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "revenue": {
                "gross": 0,
                "net": 0,
                "currency": "INR",
            },
        }
