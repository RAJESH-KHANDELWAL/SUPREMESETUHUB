"""Independent registry for infrastructure ENGINE module metadata."""
from __future__ import annotations
from .models import InfrastructureEngineModule

class InfrastructureEngineRegistry:
    def __init__(self) -> None:
        self._modules: dict[str, InfrastructureEngineModule] = {}

    def register(self, module: InfrastructureEngineModule) -> None:
        if module.module_id in self._modules:
            raise ValueError(f"Duplicate infrastructure ENGINE module: {module.module_id}")
        self._modules[module.module_id] = module

    def get(self, module_id: str) -> InfrastructureEngineModule | None:
        return self._modules.get(module_id)

    def list(self) -> tuple[InfrastructureEngineModule, ...]:
        return tuple(self._modules.values())
