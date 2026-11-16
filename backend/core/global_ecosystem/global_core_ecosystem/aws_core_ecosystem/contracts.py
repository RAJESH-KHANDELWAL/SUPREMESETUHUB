"""AWS Core contracts; AWS SDK, signing and credential resolution stay in API."""
from __future__ import annotations
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

class Readiness(str, Enum):
    CATALOG_ONLY = "CORE_CATALOG_ONLY"
    CONFIGURATION_REQUIRED = "NEEDS_CONFIGURATION"
    CONFIGURED_NOT_VERIFIED = "CONFIGURED_NOT_VERIFIED"
    READY = "READY"
    DISABLED = "DISABLED"
    ERROR = "ERROR"

@dataclass(frozen=True)
class AwsAccountContext:
    account_id: str
    region: str
    tenant_id: str
    actor_id: str
    principal_arn: str | None = None
    request_id: str | None = None
    def validate(self) -> None:
        for name, value in (("account_id", self.account_id), ("region", self.region), ("tenant_id", self.tenant_id), ("actor_id", self.actor_id)):
            if not value or not value.strip():
                raise ValueError(f"AWS_{name.upper()}_REQUIRED")
        if not self.account_id.isdigit() or len(self.account_id) != 12:
            raise ValueError("AWS_ACCOUNT_ID_MUST_BE_12_DIGITS")

@dataclass(frozen=True)
class CredentialReference:
    provider: str
    reference: str
    version: str | None = None
    def __post_init__(self) -> None:
        if self.provider.casefold() not in {"aws_secrets_manager", "aws_ssm_parameter_store", "external_secret_manager", "workload_identity"}:
            raise ValueError("AWS_CREDENTIAL_REFERENCE_PROVIDER_UNSUPPORTED")
        if not self.reference.strip():
            raise ValueError("AWS_CREDENTIAL_REFERENCE_REQUIRED")

@dataclass
class CoreResult:
    success: bool
    ecosystem_id: str
    status: str
    data: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    request_id: str | None = None
    timestamp: str = field(default_factory=utc_now)
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
