"""
MAIN BASE FOUNDATION
INFRASTRUCTURE SERVICE

Business/service layer for infrastructure resources.

Responsibilities:
- infrastructure resource registration
- resource retrieval
- resource listing
- resource deletion
- resource relationships
- resource validation

This service does NOT directly perform provider operations.

Provider/API/engine operations belong to their
respective integration and engine layers.
"""

from __future__ import annotations

from typing import Optional

from .model import (
    InfrastructureCategory,
    InfrastructureOwnershipType,
    InfrastructureRelationship,
    InfrastructureRelationshipType,
    InfrastructureResource,
    InfrastructureResourceStatus,
    InfrastructureResourceType,
)

from .repository import InfrastructureRepository


class InfrastructureService:
    """Service layer for infrastructure management."""

    def __init__(
        self,
        repository: Optional[
            InfrastructureRepository
        ] = None,
    ) -> None:

        self.repository = (
            repository
            or InfrastructureRepository()
        )

    # ==============================================================
    # INITIALIZATION
    # ==============================================================

    def initialize(self) -> dict:
        """Initialize infrastructure persistence."""

        self.repository.initialize()

        return {
            "success": True,
            "status": "INFRASTRUCTURE_READY",
        }

    # ==============================================================
    # CREATE
    # ==============================================================

    def register_resource(
        self,
        resource: InfrastructureResource,
    ) -> InfrastructureResource:
        """
        Register a new infrastructure resource.

        Validation is performed before persistence.
        """

        self._validate_resource(
            resource
        )

        existing = self.repository.get(
            resource.resource_id
        )

        if existing is not None:
            raise ValueError(
                "Infrastructure resource already exists: "
                f"{resource.resource_id}"
            )

        return self.repository.create(
            resource
        )

    # ==============================================================
    # READ
    # ==============================================================

    def get_resource(
        self,
        resource_id: str,
    ) -> Optional[InfrastructureResource]:
        """Return one infrastructure resource."""

        return self.repository.get(
            resource_id
        )

    # ==============================================================
    # LIST
    # ==============================================================

    def list_resources(
        self,
    ) -> list[InfrastructureResource]:
        """Return all infrastructure resources."""

        return self.repository.list_all()

    # ==============================================================
    # DELETE
    # ==============================================================

    def delete_resource(
        self,
        resource_id: str,
    ) -> bool:
        """
        Delete an infrastructure resource.

        This operation only removes the platform's
        database record.

        It does NOT delete an actual external server,
        VPS, domain, hosting account, or provider resource.
        """

        resource = self.repository.get(
            resource_id
        )

        if resource is None:
            return False

        return self.repository.delete(
            resource_id
        )

    # ==============================================================
    # RELATIONSHIPS
    # ==============================================================

    def connect_resources(
        self,
        relationship: InfrastructureRelationship,
    ) -> InfrastructureRelationship:
        """
        Connect two infrastructure resources.
        """

        source = self.repository.get(
            relationship.source_resource_id
        )

        if source is None:
            raise ValueError(
                "Source infrastructure resource "
                "does not exist."
            )

        target = self.repository.get(
            relationship.target_resource_id
        )

        if target is None:
            raise ValueError(
                "Target infrastructure resource "
                "does not exist."
            )

        if (
            relationship.source_resource_id
            == relationship.target_resource_id
        ):
            raise ValueError(
                "A resource cannot be connected "
                "to itself."
            )

        return self.repository.create_relationship(
            relationship
        )

    def list_relationships(
        self,
    ) -> list[InfrastructureRelationship]:
        """Return infrastructure relationships."""

        return self.repository.list_relationships()

    # ==============================================================
    # VALIDATION
    # ==============================================================

    @staticmethod
    def _validate_resource(
        resource: InfrastructureResource,
    ) -> None:
        """Validate an infrastructure resource."""

        if not resource.resource_id:
            raise ValueError(
                "resource_id is required."
            )

        if not resource.name:
            raise ValueError(
                "resource name is required."
            )

        if not isinstance(
            resource.resource_type,
            InfrastructureResourceType,
        ):
            raise ValueError(
                "Invalid infrastructure resource type."
            )

        if not isinstance(
            resource.category,
            InfrastructureCategory,
        ):
            raise ValueError(
                "Invalid infrastructure category."
            )

        if not isinstance(
            resource.status,
            InfrastructureResourceStatus,
        ):
            raise ValueError(
                "Invalid infrastructure status."
            )

        if not isinstance(
            resource.ownership_type,
            InfrastructureOwnershipType,
        ):
            raise ValueError(
                "Invalid infrastructure ownership type."
            )

    # ==============================================================
    # TYPE FILTERS
    # ==============================================================

    def list_by_type(
        self,
        resource_type: InfrastructureResourceType,
    ) -> list[InfrastructureResource]:
        """Return resources of a specific type."""

        resources = self.repository.list_all()

        return [
            resource
            for resource in resources
            if resource.resource_type
            == resource_type
        ]

    def list_by_category(
        self,
        category: InfrastructureCategory,
    ) -> list[InfrastructureResource]:
        """Return resources of a specific category."""

        resources = self.repository.list_all()

        return [
            resource
            for resource in resources
            if resource.category
            == category
        ]

    def list_by_owner(
        self,
        owner_id: str,
    ) -> list[InfrastructureResource]:
        """Return resources belonging to an owner."""

        resources = self.repository.list_all()

        return [
            resource
            for resource in resources
            if resource.owner_id
            == owner_id
        ]

    def list_by_business(
        self,
        business_id: str,
    ) -> list[InfrastructureResource]:
        """Return resources belonging to a business."""

        resources = self.repository.list_all()

        return [
            resource
            for resource in resources
            if resource.business_id
            == business_id
        ]

    def list_by_customer(
        self,
        customer_id: str,
    ) -> list[InfrastructureResource]:
        """Return resources assigned to a customer."""

        resources = self.repository.list_all()

        return [
            resource
            for resource in resources
            if resource.customer_id
            == customer_id
        ]

    # ==============================================================
    # STATUS
    # ==============================================================

    def set_status(
        self,
        resource_id: str,
        status: InfrastructureResourceStatus,
    ) -> InfrastructureResource:
        """
        Change the logical status of a resource.

        Actual provider-side state is not changed here.
        """

        resource = self.repository.get(
            resource_id
        )

        if resource is None:
            raise ValueError(
                "Infrastructure resource not found: "
                f"{resource_id}"
            )

        resource.status = status

        # Current repository implementation has
        # create/read/delete persistence only.
        # Update persistence will be added in the
        # next database update step.

        return resource

    # ==============================================================
    # STATUS
    # ==============================================================

    def status(self) -> dict:
        """Return service status."""

        resources = self.repository.list_all()

        return {
            "service": "InfrastructureService",
            "status": "READY",
            "resource_count": len(resources),
        }


__all__ = [
    "InfrastructureService",
]
