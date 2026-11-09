"""LINKSETU channel experience service."""


class LinkSetuChannelService:
    """Manage channels in LINKSETU."""

    platform_name = "LINKSETU"

    def create_channel(
        self,
        owner_id: str,
        name: str,
        description: str = "",
        category: str = "",
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "name": name,
            "description": description,
            "category": category,
            "entity_type": "channel",
            "status": "created",
        }

    def get_channel(
        self,
        channel_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "channel_id": channel_id,
            "entity_type": "channel",
        }

    def update_channel(
        self,
        channel_id: str,
        data: dict,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "channel_id": channel_id,
            "entity_type": "channel",
            "data": data,
            "status": "updated",
        }

    def follow_channel(
        self,
        user_id: str,
        channel_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "channel_id": channel_id,
            "status": "following",
        }

    def unfollow_channel(
        self,
        user_id: str,
        channel_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "channel_id": channel_id,
            "status": "unfollowed",
        }

    def get_channels(
        self,
        owner_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "channels": [],
        }
