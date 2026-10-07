"""LINKSETU professional experience service."""


class LinkSetuProfessionalService:
    """Manage professional identity and career information in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_visibility = (
        "public",
        "connections",
        "private",
    )

    allowed_statuses = (
        "active",
        "inactive",
    )

    def create_profile(
        self,
        user_id: str,
        headline: str = "",
        summary: str = "",
        industry: str = "",
        location: str = "",
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "headline": headline,
            "summary": summary,
            "industry": industry,
            "location": location,
            "status": "active",
        }

    def get_profile(
        self,
        user_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "status": "active",
        }

    def update_profile(
        self,
        user_id: str,
        headline: str | None = None,
        summary: str | None = None,
        industry: str | None = None,
        location: str | None = None,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "headline": headline,
            "summary": summary,
            "industry": industry,
            "location": location,
            "status": "updated",
        }

    def add_experience(
        self,
        user_id: str,
        company_id: str,
        title: str,
        description: str = "",
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "company_id": company_id,
            "title": title,
            "description": description,
            "status": "added",
        }

    def add_education(
        self,
        user_id: str,
        institution: str,
        qualification: str,
        field: str = "",
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "institution": institution,
            "qualification": qualification,
            "field": field,
            "status": "added",
        }

    def add_skill(
        self,
        user_id: str,
        skill: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "skill": skill,
            "status": "added",
        }

    def get_skills(
        self,
        user_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "skills": [],
        }

    def set_visibility(
        self,
        user_id: str,
        visibility: str,
    ) -> dict:
        if visibility not in self.allowed_visibility:
            raise ValueError(
                f"Unsupported professional visibility: {visibility}"
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "visibility": visibility,
        }

    def update_status(
        self,
        user_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported professional status: {status}"
            )

        return {
            "platform": self.platform_name,
            "user_id": user_id,
            "status": status,
        }
