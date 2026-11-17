"""LINKSETU moderation experience service."""


class LinkSetuModerationService:
    """Manage platform-specific moderation in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_actions = (
        "review",
        "approve",
        "hide",
        "remove",
        "restrict",
        "restore",
    )

    def create_review(
        self,
        moderator_id: str,
        target_id: str,
        target_type: str,
        reason: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "moderator_id": moderator_id,
            "target_id": target_id,
            "target_type": target_type,
            "reason": reason,
            "status": "review_pending",
        }

    def take_action(
        self,
        moderator_id: str,
        target_id: str,
        action: str,
    ) -> dict:

        if action not in self.allowed_actions:
            raise ValueError(
                f"Unsupported moderation action: {action}"
            )

        return {
            "platform": self.platform_name,
            "moderator_id": moderator_id,
            "target_id": target_id,
            "action": action,
            "status": "action_recorded",
        }

    def get_review(
        self,
        review_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "review_id": review_id,
            "status": "pending",
        }

    def restore_content(
        self,
        moderator_id: str,
        target_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "moderator_id": moderator_id,
            "target_id": target_id,
            "action": "restore",
            "status": "restored",
        }
