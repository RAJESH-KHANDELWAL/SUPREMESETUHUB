"""LINKSETU contact experience service."""


class LinkSetuContactService:
    """Manage user contact relationships in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_statuses = (
        "active",
        "blocked",
        "removed",
    )

    def add_contact(
        self,
        user_id: str,
        contact_user_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "contact_user_id": contact_user_id,
            "status": "active",
        }

    def remove_contact(
        self,
        user_id: str,
        contact_user_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "contact_user_id": contact_user_id,
            "status": "removed",
        }

    def block_contact(
        self,
        user_id: str,
        contact_user_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "contact_user_id": contact_user_id,
            "status": "blocked",
        }

    def get_contact(
        self,
        user_id: str,
        contact_user_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "contact_user_id": contact_user_id,
            "status": "active",
        }

    def get_contacts(
        self,
        user_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "contacts": [],
        }

    def is_contact(
        self,
        user_id: str,
        contact_user_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "contact_user_id": contact_user_id,
            "is_contact": False,
        }

    def search_contacts(
        self,
        user_id: str,
        query: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "query": query,
            "contacts": [],
        }

    def update_contact_status(
        self,
        user_id: str,
        contact_user_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported contact status: {status}"
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "contact_user_id": contact_user_id,
            "status": status,
        }
