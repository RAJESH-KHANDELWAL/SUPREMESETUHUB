"""LINKSETU live experience service."""


class LinkSetuLiveService:
    """Manage live streaming experiences in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_statuses = (
        "scheduled",
        "live",
        "ended",
        "cancelled",
    )

    def create_live(
        self,
        user_id: str,
        title: str,
        description: str = "",
        scheduled_at: str | None = None,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "title": title,
            "description": description,
            "scheduled_at": scheduled_at,
            "status": "scheduled",
        }

    def get_live(self, live_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "live_id": live_id,
            "status": "live",
        }

    def start_live(self, live_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "live_id": live_id,
            "status": "live",
        }

    def end_live(self, live_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "live_id": live_id,
            "status": "ended",
        }

    def cancel_live(self, live_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "live_id": live_id,
            "status": "cancelled",
        }

    def get_live_feed(self, user_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "live_streams": [],
        }

    def join_live(
        self,
        user_id: str,
        live_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "live_id": live_id,
            "status": "joined",
        }

    def leave_live(
        self,
        user_id: str,
        live_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "live_id": live_id,
            "status": "left",
        }

    def update_live_status(
        self,
        live_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported live status: {status}"
            )

        return {
            "platform": self.platform_name,
            "live_id": live_id,
            "status": status,
        }
