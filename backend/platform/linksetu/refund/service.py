"""LINKSETU refund experience service."""


class LinkSetuRefundService:
    """Manage refund experience in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_statuses = (
        "requested",
        "processing",
        "approved",
        "rejected",
        "completed",
        "cancelled",
    )

    allowed_reasons = (
        "order_cancelled",
        "returned_item",
        "duplicate_payment",
        "payment_failure",
        "customer_request",
        "other",
    )

    def create_refund(
        self,
        payment_id: str,
        order_id: str,
        requester_id: str,
        amount: float,
        reason: str,
    ) -> dict:
        if amount <= 0:
            raise ValueError(
                "Refund amount must be greater than zero."
            )

        if reason not in self.allowed_reasons:
            raise ValueError(
                f"Unsupported refund reason: {reason}"
            )

        return {
            "platform": self.platform_name,
            "payment_id": payment_id,
            "order_id": order_id,
            "requester_id": requester_id,
            "amount": amount,
            "reason": reason,
            "status": "requested",
        }

    def get_refund(self, refund_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "refund_id": refund_id,
            "status": "requested",
        }

    def update_refund_status(
        self,
        refund_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported refund status: {status}"
            )

        return {
            "platform": self.platform_name,
            "refund_id": refund_id,
            "status": status,
        }

    def approve_refund(self, refund_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "refund_id": refund_id,
            "status": "approved",
        }

    def reject_refund(self, refund_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "refund_id": refund_id,
            "status": "rejected",
        }

    def complete_refund(self, refund_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "refund_id": refund_id,
            "status": "completed",
        }

    def cancel_refund(self, refund_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "refund_id": refund_id,
            "status": "cancelled",
        }

    def get_user_refunds(self, user_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "refunds": [],
        }
