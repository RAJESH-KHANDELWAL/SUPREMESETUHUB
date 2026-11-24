"""LINKSETU follow experience service."""


class LinkSetuFollowService:
    """Manage follow relationships in LINKSETU."""

    platform_name = "LINKSETU"

    def follow(
        self,
        follower_id: str,
        following_id: str,
    ) -> dict:

        if follower_id == following_id:
            raise ValueError(
                "A person cannot follow themselves."
            )

        return {
            "platform": self.platform_name,
            "follower_id": follower_id,
            "following_id": following_id,
            "status": "following",
        }

    def unfollow(
        self,
        follower_id: str,
        following_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "follower_id": follower_id,
            "following_id": following_id,
            "status": "unfollowed",
        }

    def get_followers(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "followers": [],
        }

    def get_following(
        self,
        user_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "following": [],
        }

    def is_following(
        self,
        follower_id: str,
        following_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "follower_id": follower_id,
            "following_id": following_id,
            "is_following": False,
        }
