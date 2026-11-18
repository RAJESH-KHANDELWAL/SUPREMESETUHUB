"""LINKSETU delivery experience service."""


class LinkSetuDeliveryService:
    """Manage delivery experience in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_statuses = (
        "pending",
        "assigned",
        "picked_up",
        "in_transit",
        "out_for_delivery",
        "delivered",
        "failed",
        "cancelled",
        "returned",
    )

    def create_delivery(
        self,
        order_id: str,
        shipment_id: str,
        recipient_id: str,
        address: str,
        delivery_date: str | None = None,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "order_id": order_id,
            "shipment_id": shipment_id,
            "recipient_id": recipient_id,
            "address": address,
            "delivery_date": delivery_date,
            "status": "pending",
        }

    def get_delivery(self, delivery_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "delivery_id": delivery_id,
            "status": "pending",
        }

    def update_delivery_status(
        self,
        delivery_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported delivery status: {status}"
            )

        return {
            "platform": self.platform_name,
            "delivery_id": delivery_id,
            "status": status,
        }

    def assign_delivery_agent(
        self,
        delivery_id: str,
        agent_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "delivery_id": delivery_id,
            "agent_id": agent_id,
            "status": "assigned",
        }

    def get_order_deliveries(self, order_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "order_id": order_id,
            "deliveries": [],
        }

    def cancel_delivery(self, delivery_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "delivery_id": delivery_id,
            "status": "cancelled",
        }

    def confirm_delivery(self, delivery_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "delivery_id": delivery_id,
            "status": "delivered",
        }
