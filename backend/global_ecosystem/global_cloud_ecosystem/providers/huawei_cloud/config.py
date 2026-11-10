"""Environment configuration for Huawei Cloud."""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class HuaweiCloudConfig:
    access_key: str | None = None
    secret_key: str | None = None
    region: str | None = None
    @classmethod
    def from_env(cls) -> "HuaweiCloudConfig":
        return cls(os.getenv("HUAWEICLOUD_ACCESS_KEY"), os.getenv("HUAWEICLOUD_SECRET_KEY"), os.getenv("HUAWEICLOUD_REGION"))
    def credentials_configured(self) -> bool:
        return bool(self.access_key and self.secret_key)
