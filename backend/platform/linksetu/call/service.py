"""LINKSETU call experience service."""


class LinkSetuCallService:
    """Manage voice and video call experiences in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_call_types = (
        "voice",
        "video",
    )

    allowed_statuses = (
        "ringing",
        "accepted",
        "active",
        "ended",
        "rejected",
        "missed",
        "cancelled",
    )

    def create_call(
        self,
        caller_id: str,
        receiver_id: str,
        call_type: str = "voice",
    ) -> dict:
        if call_type not in self.allowed_call_types:
            raise ValueError(
                f"Unsupported call type: {call_type}"
            )

        return {
            "platform": self.platform_name,
            "caller_id": caller_id,
            "receiver_id": receiver_id,
            "call_type": call_type,
            "status": "ringing",
        }

    def accept_call(self, call_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "call_id": call_id,
            "status": "accepted",
        }

    def start_call(self, call_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "call_id": call_id,
            "status": "active",
        }

    def end_call(self, call_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "call_id": call_id,
            "status": "ended",
        }

    def reject_call(self, call_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "call_id": call_id,
            "status": "rejected",
        }

    def cancel_call(self, call_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "call_id": call_id,
            "status": "cancelled",
        }

    def mark_missed(self, call_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "call_id": call_id,
            "status": "missed",
        }

    def get_call(self, call_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "call_id": call_id,
            "status": "active",
        }

    def update_call_status(
        self,
        call_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported call status: {status}"
            )

        return {
            "platform": self.platform_name,
            "call_id": call_id,
            "status": status,
        }
