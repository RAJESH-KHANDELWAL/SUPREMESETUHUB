"""Policy gates for future software integrations; no provider calls are made."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    reason: str
    required_controls: tuple[str, ...]


BASE_CONTROLS = (
    "TENANT_ISOLATION",
    "LEAST_PRIVILEGE_SCOPES",
    "EXTERNAL_SECRET_MANAGER",
    "AUDIT_TRAIL",
    "LICENSE_AND_TERMS_REVIEW",
    "DATA_PROTECTION_AND_RESIDENCY_REVIEW",
)


def evaluate_activation(*, tenant_id: str | None, scopes: tuple[str, ...],
                        secret_reference: str | None, consent_recorded: bool) -> PolicyDecision:
    missing = []
    if not tenant_id:
        missing.append("TENANT_ID")
    if not scopes:
        missing.append("LEAST_PRIVILEGE_SCOPES")
    if not secret_reference:
        missing.append("EXTERNAL_SECRET_REFERENCE")
    if not consent_recorded:
        missing.append("CONSENT_RECORD")
    if missing:
        return PolicyDecision(False, "Required controls are missing: " + ", ".join(missing), BASE_CONTROLS)
    return PolicyDecision(True, "Metadata policy checks passed; live connectivity is not implied.", BASE_CONTROLS)
