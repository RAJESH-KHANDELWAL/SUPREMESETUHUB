"""LINKSETU list experience service."""


class LinkSetuListService:
    """Manage curated user and content lists in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_visibility = (
        "public",
        "private",
        "connections",
    )

    def create_list(
        self,
        user_id: str,
        name: str,
        description: str = "",
        visibility: str = "private",
    ) -> dict:
        if visibility not in self.allowed_visibility:
            raise ValueError(
                f"Unsupported list visibility: {visibility}"
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "name": name,
            "description": description,
            "visibility": visibility,
            "status": "active",
        }

    def get_list(self, list_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "list_id": list_id,
            "status": "active",
        }

    def get_user_lists(self, user_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "lists": [],
        }

    def add_member(
        self,
        list_id: str,
        user_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "list_id": list_id,
            "user_id": user_id,
            "status": "added",
        }

    def remove_member(
        self,
        list_id: str,
        user_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "list_id": list_id,
            "user_id": user_id,
            "status": "removed",
        }

    def get_members(self, list_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "list_id": list_id,
            "members": [],
        }

    def add_post(
        self,
        list_id: str,
        post_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "list_id": list_id,
            "post_id": post_id,
            "status": "added",
        }

    def remove_post(
        self,
        list_id: str,
        post_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "list_id": list_id,
            "post_id": post_id,
            "status": "removed",
        }

    def get_list_feed(self, list_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "list_id": list_id,
            "posts": [],
        }

    def update_visibility(
        self,
        list_id: str,
        visibility: str,
    ) -> dict:
        if visibility not in self.allowed_visibility:
            raise ValueError(
                f"Unsupported list visibility: {visibility}"
            )

        return {
            "platform": self.platform_name,
            "list_id": list_id,
            "visibility": visibility,
        }

    def delete_list(self, list_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "list_id": list_id,
            "status": "deleted",
        }
