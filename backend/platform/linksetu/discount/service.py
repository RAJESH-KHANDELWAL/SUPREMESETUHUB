"""LINKSETU discount experience service."""


class LinkSetuDiscountService:
    """Manage discount experiences in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_types = (
        "percentage",
        "fixed_amount",
    )

    allowed_statuses = (
        "draft",
        "active",
        "paused",
        "expired",
        "disabled",
    )

    def create_discount(
        self,
        owner_id: str,
        name: str,
        discount_type: str,
        value: float,
        expires_at: str | None = None,
    ) -> dict:
        if discount_type not in self.allowed_types:
            raise ValueError(
                f"Unsupported discount type: {discount_type}"
            )

        if value <= 0:
            raise ValueError(
                "Discount value must be greater than zero."
            )

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "name": name,
            "discount_type": discount_type,
            "value": value,
            "expires_at": expires_at,
            "status": "draft",
        }

    def get_discount(self, discount_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "discount_id": discount_id,
            "status": "draft",
        }

    def update_discount(
        self,
        discount_id: str,
        data: dict,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "discount_id": discount_id,
            "data": data,
            "status": "updated",
        }

    def update_discount_status(
        self,
        discount_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported discount status: {status}"
            )

        return {
            "platform": self.platform_name,
            "discount_id": discount_id,
            "status": status,
        }

    def apply_discount(
        self,
        user_id: str,
        discount_id: str,
        order_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "discount_id": discount_id,
            "order_id": order_id,
            "status": "applied",
        }

    def get_owner_discounts(self, owner_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "discounts": [],
        }

    def delete_discount(self, discount_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "discount_id": discount_id,
            "status": "deleted",
        }
