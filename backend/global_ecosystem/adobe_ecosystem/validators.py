"""Shared input validation for catalog-level Adobe workflows."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


ALLOWED_MATURITY = {"basic", "standard", "professional", "enterprise", "supreme"}
ALLOWED_REGIONS = {"India", "Global"}


@dataclass(frozen=True)
class ValidationResult:
    valid: bool
    errors: tuple[str, ...] = ()


def validate_workflow_request(payload: dict[str, Any]) -> ValidationResult:
    errors: list[str] = []
    product = payload.get("product")
    operation = payload.get("operation")
    maturity = payload.get("maturity", "basic")
    regions = payload.get("regions", ["India", "Global"])
    if not isinstance(product, str) or not product.strip():
        errors.append("product must be a non-empty string")
    if not isinstance(operation, str) or not operation.strip():
        errors.append("operation must be a non-empty string")
    if maturity not in ALLOWED_MATURITY:
        errors.append("maturity is not a supported level")
    if not isinstance(regions, list) or not regions or any(r not in ALLOWED_REGIONS for r in regions):
        errors.append("regions must be a non-empty list containing India and/or Global")
    return ValidationResult(not errors, tuple(errors))
