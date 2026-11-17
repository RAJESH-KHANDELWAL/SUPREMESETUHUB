"""Executable validation and planning layer for application domains."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping
from .scope import get_domain

class DomainValidationError(ValueError):
    """Raised when a workflow fails domain safeguards."""

@dataclass(frozen=True)
class DomainWorkflowResult:
    domain_id: str
    action: str
    accepted: bool
    status: str
    checks: tuple[str, ...]
    required_safeguards: tuple[str, ...]
    provider_execution: str = "not_performed"
    def to_dict(self) -> dict[str, Any]:
        return {"domain_id": self.domain_id, "action": self.action, "accepted": self.accepted, "status": self.status, "checks": list(self.checks), "required_safeguards": list(self.required_safeguards), "provider_execution": self.provider_execution}

class AppDomainService:
    ALLOWED_ACTIONS = frozenset({"inspect", "validate", "plan"})
    def __init__(self, domain_id: str) -> None:
        self.profile = get_domain(domain_id)
        if self.profile is None:
            raise KeyError(f"Unknown application domain: {domain_id}")
        self.domain_id = domain_id
    def inspect(self) -> dict[str, Any]:
        return {**self.profile, "implementation_status": "domain_workflow_service_available", "provider_execution": "not_connected", "supported_actions": sorted(self.ALLOWED_ACTIONS)}
    def validate(self, payload: Mapping[str, Any]) -> DomainWorkflowResult:
        if not isinstance(payload, Mapping):
            raise DomainValidationError("payload must be a mapping")
        action = str(payload.get("action", "validate")).strip().lower()
        if action not in self.ALLOWED_ACTIONS:
            raise DomainValidationError(f"Unsupported action: {action}")
        checks = ["payload_shape_valid", "domain_registered"]
        safeguards = tuple(self.profile.get("safeguards", ()))
        adult = self.domain_id.startswith("adult_") or self.domain_id == "adult_age_restricted_platform_apps"
        rights_domain = any(x in self.domain_id for x in ("adult_age_restricted", "adult_creator", "adult_entertainment", "adult_content_safety"))
        if adult:
            required = {"age_verified": "age verification", "participants_are_adults": "adult participants", "consent_confirmed": "informed consent"}
            for key, label in required.items():
                if payload.get(key) is not True:
                    raise DomainValidationError(f"{key}=true is required ({label})")
            checks.extend(["adult_age_gate_confirmed", "adult_participants_confirmed", "informed_consent_confirmed"])
            if rights_domain:
                if payload.get("rights_cleared") is not True:
                    raise DomainValidationError("rights_cleared=true is required")
                if payload.get("nonconsensual_intimate_content") is True:
                    raise DomainValidationError("non-consensual intimate content is prohibited")
                checks.extend(["content_rights_confirmed", "nonconsensual_content_screened"])
            if payload.get("exploitation_detected") is True:
                raise DomainValidationError("exploitation or trafficking indicators block this workflow")
            checks.append("exploitation_screen_passed")
            classification = payload.get("content_classification")
            if classification is not None:
                if not isinstance(classification, Mapping):
                    raise DomainValidationError("content_classification must be a mapping")
                label = str(classification.get("orientation_label", "UNSPECIFIED")).strip().upper()
                if label not in {"STRAIGHT", "GAY", "BISEXUAL", "OTHER", "UNSPECIFIED"}:
                    raise DomainValidationError("unknown orientation content label")
                if label != "UNSPECIFIED":
                    if str(classification.get("classification_subject_type", "")).strip().upper() not in {"CREATOR", "PERFORMER"}:
                        raise DomainValidationError("creator/performer classification subject required")
                    if str(classification.get("orientation_source", "")).strip().upper() not in {"SELF_DECLARED", "AUTHORIZED_RIGHTS_HOLDER"}:
                        raise DomainValidationError("self-declared or authorised provenance required")
                    if classification.get("orientation_inferred") is True:
                        raise DomainValidationError("orientation inference is prohibited")
                    if not str(classification.get("consent_record_reference", "")).strip():
                        raise DomainValidationError("consent record reference required")
                    if not str(classification.get("rights_record_reference", "")).strip():
                        raise DomainValidationError("rights record reference required")
                if "viewer_orientation_profile" in classification or classification.get("viewer_orientation_profile") is not None:
                    raise DomainValidationError("viewer orientation profiling is prohibited")
                checks.append("content_classification_metadata_validated")
        if self.domain_id == "sexual_wellness_education_apps" and payload.get("privacy_controls_enabled") is not True:
            raise DomainValidationError("privacy_controls_enabled=true is required")
        if self.domain_id == "healthcare_wellness_fitness_apps" and payload.get("clinical_scope_acknowledged") is not True:
            raise DomainValidationError("clinical_scope_acknowledged=true is required")
        if self.domain_id == "banking_finance_payment_apps" and payload.get("financial_compliance_acknowledged") is not True:
            raise DomainValidationError("financial_compliance_acknowledged=true is required")
        if self.domain_id == "sexual_wellness_education_apps": checks.append("privacy_controls_confirmed")
        if self.domain_id == "healthcare_wellness_fitness_apps": checks.append("clinical_scope_acknowledged")
        if self.domain_id == "banking_finance_payment_apps": checks.append("financial_compliance_acknowledged")
        return DomainWorkflowResult(self.domain_id, action, True, "validated_for_planning_only", tuple(checks), safeguards)
    def plan(self, payload: Mapping[str, Any]) -> dict[str, Any]:
        result = self.validate({**dict(payload), "action": "plan"})
        return {**result.to_dict(), "implementation_steps": ["confirm requirements and jurisdictions", "complete privacy, security and accessibility review", "document provider API permissions", "implement sandbox integration and automated tests", "complete legal and operational review before production"], "production_ready": False}

def create_domain_service(domain_id: str) -> AppDomainService:
    return AppDomainService(domain_id)

__all__ = ["DomainValidationError", "DomainWorkflowResult", "AppDomainService", "create_domain_service"]
