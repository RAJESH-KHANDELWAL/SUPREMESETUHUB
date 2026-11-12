"""Business domain controller facade."""
from __future__ import annotations
from typing import Any
from backend.database.service import DatabaseService
from .service import BusinessService

class BusinessController:
    def __init__(self, service: BusinessService | None = None, database: DatabaseService | None = None) -> None:
        self.service = service or BusinessService(database)

    def list(self) -> list[Any]:
        return self.service.list_businesses()

    def get(self, business_id: str) -> Any:
        return self.service.get_business(business_id)

    def create(self, **values: Any) -> Any:
        return self.service.create_business(**values)

    def update_status(self, business_id: str, status: str) -> Any:
        return self.service.update_status(business_id, status)

    def verify(self, business_id: str) -> Any:
        return self.service.verify_business(business_id)

    def delete(self, business_id: str) -> bool:
        return self.service.delete_business(business_id)
