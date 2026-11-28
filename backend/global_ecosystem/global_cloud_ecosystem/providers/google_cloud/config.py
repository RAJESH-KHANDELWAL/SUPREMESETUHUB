"""Google Cloud configuration using Application Default Credentials conventions."""
from dataclasses import dataclass
import os


@dataclass(frozen=True)
class GoogleCloudConfig:
    project_id: str | None = None
    credentials_file: str | None = None
    region: str = "asia-south1"

    @classmethod
    def from_env(cls) -> "GoogleCloudConfig":
        return cls(
            project_id=os.getenv("GOOGLE_CLOUD_PROJECT") or os.getenv("GCLOUD_PROJECT"),
            credentials_file=os.getenv("GOOGLE_APPLICATION_CREDENTIALS"),
            region=os.getenv("GOOGLE_CLOUD_REGION", "asia-south1"),
        )

    def project_configured(self) -> bool:
        return bool(self.project_id)
