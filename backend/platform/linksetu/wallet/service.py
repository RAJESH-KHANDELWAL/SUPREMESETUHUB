"""LINKSETU wallet experience service."""


class LinkSetuWalletService:
    """Manage wallet experience in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_statuses = (
        "active",
        "blocked",
        "suspended",
        "closed",
    )

    def create_wallet(self, user_id: str, currency: str = "INR") -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "currency": currency,
            "balance": 0.0,
            "status": "active",
        }

    def get_wallet(self, user_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "currency": "INR",
            "balance": 0.0,
            "status": "active",
        }

    def credit_wallet(
        self,
        user_id: str,
        amount: float,
        reference_id: str | None = None,
    ) -> dict:
        if amount <= 0:
            raise ValueError("Credit amount must be greater than zero.")

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "amount": amount,
            "reference_id": reference_id,
            "transaction_type": "credit",
            "status": "recorded",
        }

    def debit_wallet(
        self,
        user_id: str,
        amount: float,
        reference_id: str | None = None,
    ) -> dict:
        if amount <= 0:
            raise ValueError("Debit amount must be greater than zero.")

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "amount": amount,
            "reference_id": reference_id,
            "transaction_type": "debit",
            "status": "recorded",
        }

    def get_wallet_transactions(self, user_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "transactions": [],
        }

    def update_wallet_status(
        self,
        user_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported wallet status: {status}"
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "status": status,
        }
