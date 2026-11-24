"""LINKSETU message experience service."""


class LinkSetuMessageService:
    """Manage direct messaging experience in LINKSETU."""

    platform_name = "LINKSETU"

    def send_message(
        self,
        sender_id: str,
        receiver_id: str,
        content: str,
    ) -> dict:

        if sender_id == receiver_id:
            raise ValueError(
                "A person cannot send a direct message to themselves."
            )

        return {
            "platform": self.platform_name,
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "content": content,
            "status": "sent",
        }

    def get_conversation(
        self,
        user_id: str,
        other_user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "other_user_id": other_user_id,
            "messages": [],
        }

    def get_conversations(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "conversations": [],
        }

    def delete_message(
        self,
        message_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "message_id": message_id,
            "status": "deleted",
        }
