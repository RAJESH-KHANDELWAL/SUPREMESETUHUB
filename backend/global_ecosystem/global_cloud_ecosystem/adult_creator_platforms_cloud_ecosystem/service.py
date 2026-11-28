"""Executable workload service for this cloud ecosystem package."""
from __future__ import annotations
from typing import Any
from ..workloads import get_cloud_workload

PACKAGE_ID = __package__.rsplit(".", 1)[-1]
WORKLOAD_ID = PACKAGE_ID.removesuffix("_cloud_ecosystem")

class WorkloadValidationError(ValueError):
    """Raised when a workload request fails policy validation."""

def inspect() -> dict[str, Any]:
    record = get_cloud_workload(WORKLOAD_ID)
    if record is None:
        raise LookupError(f"Unknown cloud workload: {WORKLOAD_ID}")
    return record

def validate(payload: dict[str, Any]) -> dict[str, Any]:
    """Validate workload safeguards without provisioning resources."""
    if not isinstance(payload, dict):
        raise WorkloadValidationError("payload must be a dictionary")
    record = inspect()
    checks = {
        "adults_only_age_assurance": "age_verified",
        "documented_informed_consent": "consent_confirmed",
        "content_and_distribution_rights_cleared": "rights_cleared",
        "block_minors_and_nonconsensual_intimate_content": "content_safety_confirmed",
        "anti_exploitation_and_takedown_workflows": "anti_exploitation_controls",
        "privacy_security_and_legal_compliance": "privacy_and_legal_controls",
    }
    missing = [checks[key] for key in record["guardrails"] if key in checks and payload.get(checks[key]) is not True]
    if missing:
        raise WorkloadValidationError("required safeguards not confirmed: " + ", ".join(missing))
    if record["adult_industry"]:
        if payload.get("participants_are_adults") is not True:
            raise WorkloadValidationError("all participants must be verified adults")
        if payload.get("nonconsensual_intimate_content") is True:
            raise WorkloadValidationError("non-consensual intimate content is prohibited")
        if payload.get("exploitation_indicator") is True:
            raise WorkloadValidationError("suspected exploitation is prohibited")
    return {"workload_id": WORKLOAD_ID, "status": "validated_for_planning_only", "provider_execution": "not_performed"}

def plan(payload: dict[str, Any]) -> dict[str, Any]:
    """Return a policy-checked plan descriptor, not a live deployment."""
    result = validate(payload)
    record = inspect()
    return {**result, "tier": record["tier"], "regions": record["regions"], "workloads": record["workloads"], "adult_industry": record["adult_industry"], "execution_mode": "planning_only"}

__all__ = ["PACKAGE_ID", "WORKLOAD_ID", "WorkloadValidationError", "inspect", "validate", "plan"]
