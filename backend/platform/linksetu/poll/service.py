"""LINKSETU poll experience service."""


class LinkSetuPollService:
    """Manage polls in LINKSETU."""

    platform_name = "LINKSETU"

    def create_poll(
        self,
        user_id: str,
        question: str,
        options: list[str],
    ) -> dict:

        if len(options) < 2:
            raise ValueError(
                "A poll must have at least two options."
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "question": question,
            "options": options,
            "status": "created",
        }

    def vote(
        self,
        user_id: str,
        poll_id: str,
        option: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "poll_id": poll_id,
            "option": option,
            "status": "voted",
        }

    def get_poll(
        self,
        poll_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "poll_id": poll_id,
            "question": "",
            "options": [],
            "results": {},
        }

    def close_poll(
        self,
        poll_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "poll_id": poll_id,
            "status": "closed",
        }
