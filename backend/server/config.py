"""Configuration for the independent SERVER domain."""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class ServerConfig:
    environment: str = os.getenv("SERVER_ENVIRONMENT", "development")
    host: str = os.getenv("SERVER_HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", os.getenv("SERVER_PORT", "8000")))
    provider_mode: str = os.getenv("SERVER_PROVIDER_MODE", "catalog")
    region: str = os.getenv("SERVER_REGION", "global")
    def describe(self):
        return {"environment": self.environment, "host": self.host, "port": self.port,
                "provider_mode": self.provider_mode, "region": self.region}
