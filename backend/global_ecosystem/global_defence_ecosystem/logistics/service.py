"""Civilian relief supply request metadata; no procurement execution."""
from __future__ import annotations

_CATEGORIES = ("food", "safe_water", "shelter", "medical_supplies",
               "accessible_transport", "hygiene", "communications", "power")

def resource_categories() -> tuple[str, ...]:
    return _CATEGORIES

def build_supply_request(request_id: str, category: str, quantity: float, unit: str) -> dict[str, object]:
    if category not in _CATEGORIES:
        raise ValueError("Unsupported relief resource category")
    if not request_id.strip() or not unit.strip() or quantity <= 0:
        raise ValueError("request_id, positive quantity and unit are required")
    return {"request_id": request_id.strip(), "category": category,
            "quantity": quantity, "unit": unit.strip(),
            "status": "DRAFT_REQUIRES_AUTHORIZATION"}
