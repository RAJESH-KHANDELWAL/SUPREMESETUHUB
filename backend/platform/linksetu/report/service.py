"""LINKSETU report experience service."""


class LinkSetuReportService:
    """Manage reporting of users and content in LINKSETU."""

    platform_name = "LINKSETU"

    allowed_targets = (
        "user",
        "post",
        "comment",
        "message",
    )

    allowed_reasons = (
        "spam",
        "harassment",
        "abuse",
        "misinformation",
        "fraud",
        "inappropriate_content",
        "other",
    )

    def create_report(
        self,
        reporter_id: str,
        target_id: str,
        target_type: str,
        reason: str,
        description: str = "",
    ) -> dict:

        if target_type not in self.allowed_targets:
            raise ValueError(
                f"Unsupported report target: {target_type}"
            )

        if reason not in self.allowed_reasons:
            raise ValueError(
                f"Unsupported report reason: {reason}"
            )

        return {
            "platform": self.platform_name,
            "reporter_id": reporter_id,
            "target_id": target_id,
            "target_type": target_type,
            "reason": reason,
            "description": description,
            "status": "submitted",
        }

    def get_report_status(
        self,
        report_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "report_id": report_id,
            "status": "submitted",
        }
