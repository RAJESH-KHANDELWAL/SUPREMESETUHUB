"""LINKSETU order experience service."""


class LinkSetuOrderService:
    """Manage order lifecycle in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_statuses = (
        "created",
        "confirmed",
        "processing",
        "shipped",
        "delivered",
        "cancelled",
        "refunded",
    )

    def create_order(
        self,
        buyer_id: str,
        seller_id: str,
        listing_id: str,
        quantity: int = 1,
    ) -> dict:
        if quantity < 1:
            raise ValueError("Order quantity must be at least 1.")

        return {
            "platform": self.platform_name,
            "buyer_id": buyer_id,
            "seller_id": seller_id,
            "listing_id": listing_id,
            "quantity": quantity,
            "status": "created",
        }

    def get_order(self, order_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "order_id": order_id,
            "status": "created",
        }

    def update_order_status(
        self,
        order_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported order status: {status}"
            )

        return {
            "platform": self.platform_name,
            "order_id": order_id,
            "status": status,
        }

    def cancel_order(self, order_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "order_id": order_id,
            "status": "cancelled",
        }

    def get_buyer_orders(self, buyer_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "buyer_id": buyer_id,
            "orders": [],
        }

    def get_seller_orders(self, seller_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "seller_id": seller_id,
            "orders": [],
        }
