"""LINKSETU shipping experience service."""


class LinkSetuShippingService:
    """Manage shipping experience in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_statuses = (
        "pending",
        "processing",
        "shipped",
        "in_transit",
        "out_for_delivery",
        "delivered",
        "cancelled",
        "returned",
    )

    def create_shipment(
        self,
        order_id: str,
        seller_id: str,
        buyer_id: str,
        address: str,
        carrier: str | None = None,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "order_id": order_id,
            "seller_id": seller_id,
            "buyer_id": buyer_id,
            "address": address,
            "carrier": carrier,
            "status": "pending",
        }

    def get_shipment(self, shipment_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "shipment_id": shipment_id,
            "status": "pending",
        }

    def update_shipment_status(
        self,
        shipment_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported shipping status: {status}"
            )

        return {
            "platform": self.platform_name,
            "shipment_id": shipment_id,
            "status": status,
        }

    def assign_carrier(
        self,
        shipment_id: str,
        carrier: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "shipment_id": shipment_id,
            "carrier": carrier,
            "status": "assigned",
        }

    def get_order_shipments(self, order_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "order_id": order_id,
            "shipments": [],
        }

    def cancel_shipment(self, shipment_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "shipment_id": shipment_id,
            "status": "cancelled",
        }
