"""AWS Core contracts; SDK, signing and credential resolution stay in AWS API."""
from __future__ import annotations

import re
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
    """Trusted caller/account context supplied by the application layer."""

    account_id: str
    region: str
    tenant_id: str
    actor_id: str
    principal_arn: str | None = None
    request_id: str | None = None

    def validate(self) -> None:
        required = (
            ("account_id", self.account_id),
            ("region", self.region),
            ("tenant_id", self.tenant_id),
            ("actor_id", self.actor_id),
        )
        for name, value in required:
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"AWS_{name.upper()}_REQUIRED")

        account_id = self.account_id.strip()
        if not re.fullmatch(r"\d{12}", account_id):
            raise ValueError("AWS_ACCOUNT_ID_MUST_BE_12_DIGITS")

        region = self.region.strip()
        if not re.fullmatch(r"[a-z]{2}(?:-[a-z0-9]+)+-\d", region):
            raise ValueError("AWS_REGION_FORMAT_INVALID")

        if self.principal_arn:
            match = re.match(
                r"^arn:(?:aws|aws-us-gov|aws-cn):(?:iam|sts)::(\d{12}):",
                self.principal_arn.strip(),
            )
            if not match:
                raise ValueError("AWS_PRINCIPAL_ARN_INVALID")
            if match.group(1) != account_id:
                raise ValueError("AWS_PRINCIPAL_ACCOUNT_MISMATCH")


@dataclass(frozen=True)
class CredentialReference:
    """Opaque secret-manager/workload-identity reference, never secret bytes."""

    provider: str
    reference: str
    version: str | None = None

    def __post_init__(self) -> None:
        allowed = {
            "aws_secrets_manager",
            "aws_ssm_parameter_store",
            "external_secret_manager",
            "workload_identity",
        }
        if not isinstance(self.provider, str) or self.provider.casefold() not in allowed:
            raise ValueError("AWS_CREDENTIAL_REFERENCE_PROVIDER_UNSUPPORTED")
        if not isinstance(self.reference, str) or not self.reference.strip():
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
