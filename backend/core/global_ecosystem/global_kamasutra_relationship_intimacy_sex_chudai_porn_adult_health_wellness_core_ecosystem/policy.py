"""Safety and authorization boundaries for adult-wellness Core metadata."""
from __future__ import annotations

from typing import Any
from .contracts import AdultAccessAttestation, TenantContext

POLICY = {
    "adult_only": True,
    "minimum_age": 18,
    "age_assurance_required": True,
    "informed_consent_required": True,
    "rights_verification_required": True,
    "non_consensual_intimate_content_prohibited": True,
    "minors_and_child_sexual_abuse_material_prohibited": True,
    "exploitation_trafficking_and_coercion_prohibited": True,
    "privacy_by_design_required": True,
    "sensitive_health_data_prohibited_in_core_catalog": True,
    "clinical_services_require_licensed_professionals": True,
    "catalog_registration_is_not_provider_approval": True,
}


class KamasutraCorePolicyError(PermissionError):
    """Raised when a request violates a mandatory Core safety boundary."""


def get_policy() -> dict[str, object]:
    return dict(POLICY)


def validate_adult_access(
    context: TenantContext | None,
    attestation: AdultAccessAttestation | None,
) -> dict[str, Any]:
    """Validate trusted upstream attestations; this function does not verify identity itself."""
    try:
        if context is None:
            raise ValueError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        context.validate()
        if attestation is None:
            raise ValueError("ADULT_ACCESS_ATTESTATION_REQUIRED")
        attestation.validate()
    except ValueError as exc:
        raise KamasutraCorePolicyError(str(exc)) from exc
    return {
        "success": True,
        "tenant_id": context.tenant_id,
        "actor_id": context.actor_id,
        "verified_by": attestation.verified_by,
        "api_call_performed": False,
    }


__all__ = ["POLICY", "KamasutraCorePolicyError", "get_policy", "validate_adult_access"]
