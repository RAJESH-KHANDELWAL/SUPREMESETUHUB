"""
LINKSETU PROFILE SERVICE
"""


class ProfileService:

    def create_profile(
        self,
        user_id: str,
        username: str,
        display_name: str,
        bio: str = "",
    ):
        return {
            "user_id": user_id,
            "username": username,
            "display_name": display_name,
            "bio": bio,
            "platform": "LINKSETU",
            "status": "created",
        }

    def get_profile(self, user_id: str):
        return {
            "platform": "LINKSETU",
            "user_id": user_id,
        }

    def update_profile(self, user_id: str, **updates):
        return {
            "platform": "LINKSETU",
            "user_id": user_id,
            "updates": updates,
            "status": "updated",
        }
