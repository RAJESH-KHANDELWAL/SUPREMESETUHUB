"""LINKSETU job experience service."""


class LinkSetuJobService:
    """Manage professional job opportunities in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_statuses = (
        "draft",
        "open",
        "paused",
        "closed",
        "archived",
    )

    allowed_types = (
        "full_time",
        "part_time",
        "contract",
        "freelance",
        "internship",
        "remote",
    )

    def create_job(
        self,
        employer_id: str,
        title: str,
        description: str = "",
        job_type: str = "full_time",
        location: str = "",
    ) -> dict:
        if job_type not in self.allowed_types:
            raise ValueError(
                f"Unsupported job type: {job_type}"
            )

        return {
            "platform": self.platform_name,
            "employer_id": employer_id,
            "title": title,
            "description": description,
            "job_type": job_type,
            "location": location,
            "status": "draft",
        }

    def get_job(self, job_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "job_id": job_id,
            "status": "open",
        }

    def publish_job(self, job_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "job_id": job_id,
            "status": "open",
        }

    def pause_job(self, job_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "job_id": job_id,
            "status": "paused",
        }

    def close_job(self, job_id: str) -> dict:
        return {
            "platform": self.platform_name,
            "job_id": job_id,
            "status": "closed",
        }

    def search_jobs(
        self,
        query: str,
        location: str = "",
        job_type: str | None = None,
    ) -> dict:
        if job_type is not None and job_type not in self.allowed_types:
            raise ValueError(
                f"Unsupported job type: {job_type}"
            )

        return {
            "platform": self.platform_name,
            "query": query,
            "location": location,
            "job_type": job_type,
            "jobs": [],
        }

    def apply_for_job(
        self,
        job_id: str,
        applicant_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "job_id": job_id,
            "applicant_id": applicant_id,
            "status": "applied",
        }

    def get_applications(
        self,
        job_id: str,
    ) -> dict:
        return {
            "platform": self.platform_name,
            "job_id": job_id,
            "applications": [],
        }

    def update_job_status(
        self,
        job_id: str,
        status: str,
    ) -> dict:
        if status not in self.allowed_statuses:
            raise ValueError(
                f"Unsupported job status: {status}"
            )

        return {
            "platform": self.platform_name,
            "job_id": job_id,
            "status": status,
        }
