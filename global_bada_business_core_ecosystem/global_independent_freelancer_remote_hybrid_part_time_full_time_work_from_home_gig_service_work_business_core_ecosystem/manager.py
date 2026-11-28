"""Stable manager interface for the Bada Business service-work package."""
from __future__ import annotations

from typing import Any

from .catalog import (
    ECOSYSTEM_ID,
    get_catalog,
    get_work_model,
    list_business_capabilities,
    list_work_models,
)


class GlobalIndependentWorkServiceBusinessCoreManager:
    NAME = "GLOBAL INDEPENDENT FREELANCER REMOTE HYBRID PART TIME FULL TIME WORK FROM HOME GIG SERVICE WORK BUSINESS CORE ECOSYSTEM"
    ECOSYSTEM_ID = ECOSYSTEM_ID

    def status(self) -> dict[str, Any]:
        return get_catalog()

    def list_work_models(self) -> list[dict[str, str]]:
        return list_work_models()

    def get_work_model(self, model_id: str) -> dict[str, str] | None:
        return get_work_model(model_id)

    def list_business_capabilities(self) -> list[dict[str, str]]:
        return list_business_capabilities()


def get_manager() -> GlobalIndependentWorkServiceBusinessCoreManager:
    return GlobalIndependentWorkServiceBusinessCoreManager()


__all__ = ["get_manager", "GlobalIndependentWorkServiceBusinessCoreManager"]
