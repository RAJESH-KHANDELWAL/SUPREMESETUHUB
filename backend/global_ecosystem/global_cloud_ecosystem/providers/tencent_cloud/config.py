"""Environment configuration for Tencent Cloud."""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class TencentCloudConfig:
    access_key: str | None = None
    secret_key: str | None = None
    region: str | None = None
    @classmethod
    def from_env(cls) -> "TencentCloudConfig":
        return cls(os.getenv("TENCENTCLOUD_SECRET_ID"), os.getenv("TENCENTCLOUD_SECRET_KEY"), os.getenv("TENCENTCLOUD_REGION"))
    def credentials_configured(self) -> bool:
        return bool(self.access_key and self.secret_key)
