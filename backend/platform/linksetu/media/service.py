"""LINKSETU media experience service."""


class LinkSetuMediaService:
    """Manage media experience in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_media_types = (
        "image",
        "video",
        "audio",
        "document",
    )

    def upload_media(
        self,
        user_id: str,
        media_type: str,
        file_name: str,
    ) -> dict:

        if media_type not in self.allowed_media_types:
            raise ValueError(
                f"Unsupported media type: {media_type}"
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "media_type": media_type,
            "file_name": file_name,
            "status": "uploaded",
        }

    def get_media(
        self,
        media_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "media_id": media_id,
        }

    def delete_media(
        self,
        media_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "media_id": media_id,
            "status": "deleted",
        }

    def get_user_media(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "media": [],
        }
