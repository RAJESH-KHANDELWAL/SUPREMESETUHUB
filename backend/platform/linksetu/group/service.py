"""LINKSETU group experience service."""


class LinkSetuGroupService:
    """Manage groups in LINKSETU."""

    platform_name = "LINKSETU"

    def create_group(
        self,
        user_id: str,
        name: str,
        description: str = "",
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": user_id,
            "name": name,
            "description": description,
            "status": "created",
        }

    def get_group(
        self,
        group_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "group_id": group_id,
        }

    def join_group(
        self,
        user_id: str,
        group_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "group_id": group_id,
            "status": "joined",
        }

    def leave_group(
        self,
        user_id: str,
        group_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "group_id": group_id,
            "status": "left",
        }

    def get_groups(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "groups": [],
        }
