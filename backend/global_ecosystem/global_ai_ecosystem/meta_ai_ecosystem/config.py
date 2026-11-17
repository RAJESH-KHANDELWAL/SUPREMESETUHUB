"""Environment-backed configuration for Meta AI; never stores secrets in source."""
from __future__ import annotations

import os
from dataclasses import dataclass

from .catalog import PROVIDER


@dataclass(frozen=True, slots=True)
class ProviderConfig:
    credential: str | None
    endpoint: str | None
    region: str | None = None

    @classmethod
    def from_env(cls) -> "ProviderConfig":
        credential_name = PROVIDER["credential_env"]
        credential = os.getenv(credential_name) if credential_name else None
        endpoint = os.getenv("META_AI_ACCESS_ENDPOINT") or PROVIDER["api_endpoint"]
        region = os.getenv("AWS_REGION") if PROVIDER["id"] == "aws_bedrock" else None
        return cls(credential=credential, endpoint=endpoint, region=region)

    def validate(self) -> None:
        if PROVIDER["id"] == "aws_bedrock":
            if not self.region:
                raise RuntimeError("AWS_REGION is required for AWS Bedrock.")
            return  # AWS SDK credential chain is resolved by the Bedrock adapter.
        if not self.credential:
            raise RuntimeError(f"Set {PROVIDER['credential_env']} before using {PROVIDER['name']}.")
        if not self.endpoint:
            raise RuntimeError(f"Configure the endpoint for {PROVIDER['name']}.")
