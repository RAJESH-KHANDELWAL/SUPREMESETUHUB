"""Stable manager interface for GLOBAL INDEPENDENT FREELANCER REMOTE HYBRID PART TIME FULL TIME WORK FROM HOME GIG CORE ECOSYSTEM."""
from __future__ import annotations
from typing import Any
from .catalog import ECOSYSTEM_ID, get_catalog, list_work_models, get_work_model

class GlobalIndependentWorkCoreManager:
    NAME = "GLOBAL INDEPENDENT FREELANCER REMOTE HYBRID PART TIME FULL TIME WORK FROM HOME GIG CORE ECOSYSTEM"
    ECOSYSTEM_ID = ECOSYSTEM_ID

    def status(self) -> dict[str, Any]:
        return get_catalog()

    def list_work_models(self) -> list[dict[str, str]]:
        return list_work_models()

    def get_work_model(self, model_id: str) -> dict[str, str] | None:
        return get_work_model(model_id)

def get_manager():
    return GlobalIndependentWorkCoreManager()

__all__ = ["get_manager", "GlobalIndependentWorkCoreManager"]
