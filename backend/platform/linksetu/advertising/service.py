"""LINKSETU advertising experience service."""


class LinkSetuAdvertisingService:
    """Manage advertising experience in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_statuses = (
        "draft",
        "active",
        "paused",
        "completed",
    )

    def create_campaign(
        self,
        owner_id: str,
        name: str,
        budget: float = 0.0,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "name": name,
            "budget": budget,
            "status": "draft",
        }

    def update_campaign(
        self,
        campaign_id: str,
        data: dict,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "campaign_id": campaign_id,
            "data": data,
            "status": "updated",
        }

    def set_campaign_status(
        self,
        campaign_id: str,
        status: str,
    ) -> dict:

        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported campaign status: {status}"
            )

        return {
            "platform": self.platform_name,
            "campaign_id": campaign_id,
            "status": status,
        }

    def get_campaign(
        self,
        campaign_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "campaign_id": campaign_id,
        }

    def get_campaign_analytics(
        self,
        campaign_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "campaign_id": campaign_id,
            "analytics": {
                "impressions": 0,
                "clicks": 0,
                "conversions": 0,
                "spend": 0,
            },
        }
