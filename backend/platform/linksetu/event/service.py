"""LINKSETU event experience service."""


class LinkSetuEventService:
    """Manage events in LINKSETU."""

    platform_name = "LINKSETU"

    def create_event(
        self,
        user_id: str,
        title: str,
        description: str,
        event_date: str,
        location: str | None = None,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "title": title,
            "description": description,
            "event_date": event_date,
            "location": location,
            "status": "created",
        }

    def get_event(
        self,
        event_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "event_id": event_id,
        }

    def join_event(
        self,
        user_id: str,
        event_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "event_id": event_id,
            "status": "joined",
        }

    def leave_event(
        self,
        user_id: str,
        event_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "event_id": event_id,
            "status": "left",
        }

    def get_events(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "events": [],
        }
