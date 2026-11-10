"""Environment configuration for Alibaba Cloud."""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class AlibabaCloudConfig:
    access_key_id: str | None = None
    access_key_secret: str | None = None
    region: str | None = None

    @classmethod
    def from_env(cls) -> "AlibabaCloudConfig":
        return cls(os.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"), os.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"), os.getenv("ALIBABA_CLOUD_REGION"))

    def credentials_configured(self) -> bool:
        return bool(self.access_key_id and self.access_key_secret)
