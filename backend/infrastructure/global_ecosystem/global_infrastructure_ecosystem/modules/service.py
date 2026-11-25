"""Canonical infrastructure resource service in Global Infrastructure Ecosystem."""
from __future__ import annotations
from typing import Optional
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.model import InfrastructureCategory, InfrastructureOwnershipType, InfrastructureRelationship, InfrastructureRelationshipType, InfrastructureResource, InfrastructureResourceStatus, InfrastructureResourceType
from .repository import InfrastructureRepository

class InfrastructureService:
    def __init__(self, repository: Optional[InfrastructureRepository] = None):
        self.repository = repository or InfrastructureRepository()

    def initialize(self) -> dict:
        self.repository.initialize()
        return {"success": True, "status": "INFRASTRUCTURE_READY"}

    def register_resource(self, resource: InfrastructureResource) -> InfrastructureResource:
        self._validate_resource(resource)
        if self.repository.get(resource.resource_id) is not None:
            raise ValueError(f"Infrastructure resource already exists: {resource.resource_id}")
        return self.repository.create(resource)

    def get_resource(self, resource_id: str) -> Optional[InfrastructureResource]:
        return self.repository.get(resource_id)

    def list_resources(self) -> list[InfrastructureResource]:
        return self.repository.list_all()

    def delete_resource(self, resource_id: str) -> bool:
        return self.repository.delete(resource_id) if self.repository.get(resource_id) is not None else False

    def connect_resources(self, relationship: InfrastructureRelationship) -> InfrastructureRelationship:
        if self.repository.get(relationship.source_resource_id) is None:
            raise ValueError("Source infrastructure resource does not exist.")
        if self.repository.get(relationship.target_resource_id) is None:
            raise ValueError("Target infrastructure resource does not exist.")
        if relationship.source_resource_id == relationship.target_resource_id:
            raise ValueError("A resource cannot be connected to itself.")
        return self.repository.create_relationship(relationship)

    def list_relationships(self) -> list[InfrastructureRelationship]:
        return self.repository.list_relationships()

    @staticmethod
    def _validate_resource(resource: InfrastructureResource) -> None:
        if not resource.resource_id: raise ValueError("resource_id is required.")
        if not resource.name: raise ValueError("resource name is required.")
        if not isinstance(resource.resource_type, InfrastructureResourceType): raise ValueError("Invalid infrastructure resource type.")
        if not isinstance(resource.category, InfrastructureCategory): raise ValueError("Invalid infrastructure category.")
        if not isinstance(resource.status, InfrastructureResourceStatus): raise ValueError("Invalid infrastructure status.")
        if not isinstance(resource.ownership_type, InfrastructureOwnershipType): raise ValueError("Invalid infrastructure ownership type.")

    def list_by_type(self, resource_type: InfrastructureResourceType) -> list[InfrastructureResource]:
        return [r for r in self.repository.list_all() if r.resource_type == resource_type]
    def list_by_category(self, category: InfrastructureCategory) -> list[InfrastructureResource]:
        return [r for r in self.repository.list_all() if r.category == category]
    def list_by_owner(self, owner_id: str) -> list[InfrastructureResource]:
        return [r for r in self.repository.list_all() if r.owner_id == owner_id]
    def list_by_business(self, business_id: str) -> list[InfrastructureResource]:
        return [r for r in self.repository.list_all() if r.business_id == business_id]
    def list_by_customer(self, customer_id: str) -> list[InfrastructureResource]:
        return [r for r in self.repository.list_all() if r.customer_id == customer_id]

    def set_status(self, resource_id: str, status: InfrastructureResourceStatus) -> InfrastructureResource:
        resource = self.repository.get(resource_id)
        if resource is None: raise ValueError(f"Infrastructure resource not found: {resource_id}")
        if not isinstance(status, InfrastructureResourceStatus): raise ValueError("Invalid infrastructure status.")
        resource.status = status
        return self.repository.update(resource)

    def status(self) -> dict:
        return {"service":"InfrastructureService","status":"READY","resource_count":len(self.repository.list_all())}

__all__ = ["InfrastructureService"]
