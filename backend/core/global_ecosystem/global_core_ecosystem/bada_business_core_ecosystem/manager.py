"""Public facade for the Bada Business CORE service."""
from __future__ import annotations
from typing import Any
from .service import BadaBusinessCoreService

class BadaBusinessCoreManager:
    def __init__(self, service: BadaBusinessCoreService | None = None) -> None:
        self.service = service or BadaBusinessCoreService()
    def status(self) -> dict[str, Any]: return self.service.status()
    def programs(self) -> dict[str, Any]: return self.service.list_programs()
    def program(self, program_id: str) -> dict[str, Any]: return self.service.get_program(program_id)
    def courses(self) -> dict[str, Any]: return self.service.list_courses()
    def search_courses(self, query: str) -> dict[str, Any]: return self.service.search_courses(query)
    def events(self) -> dict[str, Any]: return self.service.list_events()
    def links(self) -> dict[str, Any]: return self.service.list_links()
    def products(self) -> dict[str, Any]: return self.service.list_products()
    def validate_registration(self, payload: dict[str, Any]) -> dict[str, Any]: return self.service.validate_registration(payload)
