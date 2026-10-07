"""LINKSETU return experience service."""


class LinkSetuReturnService:
    """Manage return experience in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_reasons = (
        "damaged",
        "defective",
        "wrong_item",
        "not_as_described",
        "changed_mind",
        "other",
    )

    allowed_statuses = (
        "requested",
        "approved",
        "rejected",
        "pickup_scheduled",
        "picked_up",
        "received",
        "refunded",
        "cancelled",
    )

    def create_return(
        self,
        order_id: str,
        buyer_id: str,
        seller_id: str,
        reason: str,
        description: str = "",
    ) -> dict:
        if reason not in self.allowed_reasons:
            raise ValueError(
                f"Unsupported return reason: {reason}"
            )

        return {
            "platform": self.platform_name,
            "order_id": order_id,
            "buyer_id": buyer_id,
            "seller_id": seller_id,
            "reason": reason,
            "description": description,
            "status": "requested",
        }

    def get_return(self, return_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "return_id": return_id,
            "status": "requested",
        }

    def update_return_status(
        self,
        return_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported return status: {status}"
            )

        return {
            "platform": self.platform_name,
            "return_id": return_id,
            "status": status,
        }

    def approve_return(self, return_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "return_id": return_id,
            "status": "approved",
        }

    def reject_return(self, return_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "return_id": return_id,
            "status": "rejected",
        }

    def cancel_return(self, return_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "return_id": return_id,
            "status": "cancelled",
        }

    def get_buyer_returns(self, buyer_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "buyer_id": buyer_id,
            "returns": [],
        }

    def get_seller_returns(self, seller_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "seller_id": seller_id,
            "returns": [],
        }
