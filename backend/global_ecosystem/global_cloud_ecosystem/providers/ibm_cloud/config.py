"""Environment configuration for IBM Cloud."""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class IBMCloudConfig:
    access_key_id: str | None = None
    access_key_secret: str | None = None
    region: str | None = None

    @classmethod
    def from_env(cls) -> "IBMCloudConfig":
        return cls(os.getenv("IBM_CLOUD_API_KEY"), os.getenv("IBM_CLOUD_REGION"), os.getenv("IBM_CLOUD_REGION"))

    def credentials_configured(self) -> bool:
        return bool(self.access_key_id and self.access_key_secret)
