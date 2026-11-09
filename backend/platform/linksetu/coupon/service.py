"""LINKSETU coupon experience service."""


class LinkSetuCouponService:
    """Manage coupon experience in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_types = (
        "percentage",
        "fixed_amount",
    )

    allowed_statuses = (
        "draft",
        "active",
        "expired",
        "disabled",
    )

    def create_coupon(
        self,
        owner_id: str,
        code: str,
        discount_type: str,
        discount_value: float,
        expires_at: str | None = None,
    ) -> dict:
        if discount_type not in self.allowed_types:
            raise ValueError(
                f"Unsupported coupon type: {discount_type}"
            )

        if discount_value <= 0:
            raise ValueError(
                "Coupon discount value must be greater than zero."
            )

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "code": code.upper(),
            "discount_type": discount_type,
            "discount_value": discount_value,
            "expires_at": expires_at,
            "status": "draft",
        }

    def get_coupon(self, coupon_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "coupon_id": coupon_id,
            "status": "draft",
        }

    def apply_coupon(
        self,
        user_id: str,
        coupon_code: str,
        order_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "coupon_code": coupon_code.upper(),
            "order_id": order_id,
            "status": "applied",
        }

    def update_coupon_status(
        self,
        coupon_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported coupon status: {status}"
            )

        return {
            "platform": self.platform_name,
            "coupon_id": coupon_id,
            "status": status,
        }

    def delete_coupon(self, coupon_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "coupon_id": coupon_id,
            "status": "deleted",
        }

    def get_owner_coupons(self, owner_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "coupons": [],
        }
