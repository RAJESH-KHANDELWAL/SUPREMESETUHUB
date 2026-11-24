"""Token configuration for DigitalOcean; never expose token values in logs."""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class DigitalOceanConfig:
    api_token: str | None = None
    @classmethod
    def from_env(cls) -> "DigitalOceanConfig":
        return cls(os.getenv("DIGITALOCEAN_TOKEN"))
    def credentials_configured(self) -> bool:
        return bool(self.api_token)
