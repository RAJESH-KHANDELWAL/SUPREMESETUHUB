"""Classify business/data workloads into provider-neutral database domains."""
from __future__ import annotations
from typing import Any
from ..catalog import WORKLOADS, ADULT_DATA_GUARDRAILS

def classify_workload(industry: str) -> dict[str, Any]:
    """Return the known workload family for an industry key."""
    if industry not in WORKLOADS:
        raise KeyError(f"unknown workload industry: {industry}")
    result: dict[str, Any] = {"industry": industry, "workloads": list(WORKLOADS[industry])}
    if industry == "adult_and_sexual_content":
        result["required_guardrails"] = get_adult_workload_safeguards()
    return result

def get_adult_workload_safeguards() -> dict[str, str]:
    """Return strict data-protection and adult-safety requirements."""
    return dict(ADULT_DATA_GUARDRAILS)
