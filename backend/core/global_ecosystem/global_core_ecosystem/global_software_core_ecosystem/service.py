"""Public facade for the Global Software Core Ecosystem."""

from __future__ import annotations

from .module_service import SoftwareModuleService
from .orchestrator import build_plan
from .policy import evaluate_activation


class GlobalSoftwareCoreService:
    def __init__(self) -> None:
        self.modules = SoftwareModuleService()

    def discover(self) -> list[dict]:
        return self.modules.discover()

    def describe(self, provider_id: str) -> dict | None:
        return self.modules.describe(provider_id)

    def plan(self, provider_id: str, capability: str, *, tenant_id: str) -> dict:
        return build_plan(provider_id, capability, tenant_id=tenant_id)

    def evaluate_policy(self, **kwargs):
        return evaluate_activation(**kwargs)
