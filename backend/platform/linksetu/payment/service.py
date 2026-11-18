"""LINKSETU payment experience service."""


class LinkSetuPaymentService:
    """Manage payment experience in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_statuses = (
        "pending",
        "processing",
        "successful",
        "failed",
        "cancelled",
        "refunded",
    )

    allowed_methods = (
        "upi",
        "card",
        "netbanking",
        "wallet",
        "bank_transfer",
    )

    def create_payment(
        self,
        payer_id: str,
        payee_id: str,
        order_id: str,
        amount: float,
        currency: str = "INR",
        payment_method: str = "upi",
    ) -> dict:
        if amount < 0:
            raise ValueError("Payment amount cannot be negative.")

        if payment_method not in self.allowed_methods:
            raise ValueError(
                f"Unsupported payment method: {payment_method}"
            )

        return {
            "platform": self.platform_name,
            "payer_id": payer_id,
            "payee_id": payee_id,
            "order_id": order_id,
            "amount": amount,
            "currency": currency,
            "payment_method": payment_method,
            "status": "pending",
        }

    def get_payment(self, payment_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "payment_id": payment_id,
            "status": "pending",
        }

    def update_payment_status(
        self,
        payment_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported payment status: {status}"
            )

        return {
            "platform": self.platform_name,
            "payment_id": payment_id,
            "status": status,
        }

    def refund_payment(
        self,
        payment_id: str,
        amount: float | None = None,
    ) -> dict:
        if amount is not None and amount < 0:
            raise ValueError("Refund amount cannot be negative.")

        return {
            "platform": self.platform_name,
            "payment_id": payment_id,
            "refund_amount": amount,
            "status": "refunded",
        }

    def get_buyer_payments(self, payer_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "payer_id": payer_id,
            "payments": [],
        }

    def get_payee_payments(self, payee_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "payee_id": payee_id,
            "payments": [],
        }
