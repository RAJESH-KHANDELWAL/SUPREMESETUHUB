"""APP ecosystem manager; lifecycle and composition only."""
from __future__ import annotations
from typing import Any
from .service import BadaBusinessAppService

class BadaBusinessAppManager:
    def __init__(self, api_service: Any = None, ai_service: Any = None) -> None:
        self.service = BadaBusinessAppService(api_service=api_service, ai_service=ai_service)

    def initialize(self) -> dict[str, Any]:
        return self.service.configure()

    def status(self) -> dict[str, Any]:
        return self.service.status()

    def diagnostics(self) -> dict[str, Any]:
        return self.service.diagnostics()
