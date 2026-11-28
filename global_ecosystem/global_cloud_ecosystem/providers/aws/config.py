"""Environment-backed AWS configuration without importing an SDK."""
from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AWSConfig:
    access_key_id: str | None = None
    secret_access_key: str | None = None
    region: str = "ap-south-1"
    session_token: str | None = None

    @classmethod
    def from_env(cls) -> "AWSConfig":
        return cls(
            access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region=os.getenv("AWS_DEFAULT_REGION", "ap-south-1"),
            session_token=os.getenv("AWS_SESSION_TOKEN"),
        )

    def credentials_configured(self) -> bool:
        return bool(self.access_key_id and self.secret_access_key)
