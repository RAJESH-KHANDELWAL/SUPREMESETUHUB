"""LINKSETU subscription experience service."""


class LinkSetuSubscriptionService:
    """Manage subscription experiences in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_statuses = (
        "active",
        "paused",
        "cancelled",
        "expired",
    )

    def create_subscription(
        self,
        user_id: str,
        entity_id: str,
        plan_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "entity_id": entity_id,
            "plan_id": plan_id,
            "status": "active",
        }

    def get_subscription(
        self,
        subscription_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "subscription_id": subscription_id,
        }

    def update_subscription_status(
        self,
        subscription_id: str,
        status: str,
    ) -> dict:

        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported subscription status: {status}"
            )

        return {
            "platform": self.platform_name,
            "subscription_id": subscription_id,
            "status": status,
        }

    def cancel_subscription(
        self,
        subscription_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "subscription_id": subscription_id,
            "status": "cancelled",
        }

    def get_user_subscriptions(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "subscriptions": [],
        }
