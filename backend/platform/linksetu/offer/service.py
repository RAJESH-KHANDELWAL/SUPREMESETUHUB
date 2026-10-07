"""LINKSETU offer experience service."""


class LinkSetuOfferService:
    """Manage promotional offers in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_types = (
        "discount",
        "bundle",
        "free_shipping",
        "cashback",
        "limited_time",
    )

    allowed_statuses = (
        "draft",
        "active",
        "paused",
        "expired",
        "disabled",
    )

    def create_offer(
        self,
        owner_id: str,
        title: str,
        description: str = "",
        offer_type: str = "discount",
        expires_at: str | None = None,
    ) -> dict:
        if offer_type not in self.allowed_types:
            raise ValueError(
                f"Unsupported offer type: {offer_type}"
            )

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "title": title,
            "description": description,
            "offer_type": offer_type,
            "expires_at": expires_at,
            "status": "draft",
        }

    def get_offer(self, offer_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "offer_id": offer_id,
            "status": "draft",
        }

    def update_offer(
        self,
        offer_id: str,
        data: dict,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "offer_id": offer_id,
            "data": data,
            "status": "updated",
        }

    def update_offer_status(
        self,
        offer_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported offer status: {status}"
            )

        return {
            "platform": self.platform_name,
            "offer_id": offer_id,
            "status": status,
        }

    def apply_offer(
        self,
        user_id: str,
        offer_id: str,
        order_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "offer_id": offer_id,
            "order_id": order_id,
            "status": "applied",
        }

    def get_owner_offers(self, owner_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "offers": [],
        }

    def delete_offer(self, offer_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "offer_id": offer_id,
            "status": "deleted",
        }
