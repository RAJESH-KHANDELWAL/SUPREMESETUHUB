"""
MAIN BASE FOUNDATION
INFRASTRUCTURE REPOSITORY

Database persistence layer for infrastructure resources.

Responsibilities:
- create infrastructure resource
- read infrastructure resource
- update infrastructure resource
- delete infrastructure resource
- list infrastructure resources
- create resource relationships
- read resource relationships

This layer does NOT:
- provision VPS
- create dedicated servers
- register domains
- modify DNS
- connect WordPress
- call external hosting APIs

Those operations belong to service / engine / integration layers.
"""

from __future__ import annotations

import json
from typing import Optional

from backend.database.service import DatabaseService

from .model import (
    InfrastructureCategory,
    InfrastructureOwnershipType,
    InfrastructureRelationship,
    InfrastructureRelationshipType,
    InfrastructureResource,
    InfrastructureResourceStatus,
    InfrastructureResourceType,
)


class InfrastructureRepository:
    """Persistent database repository for infrastructure resources."""

    RESOURCE_TABLE = "infrastructure_resources"
    RELATIONSHIP_TABLE = "infrastructure_relationships"

    def __init__(
        self,
        database_service: Optional[DatabaseService] = None,
    ) -> None:
        self.database = (
            database_service
            or DatabaseService()
        )

    # ==============================================================
    # INITIALIZATION
    # ==============================================================

    def initialize(self) -> None:
        """Create infrastructure persistence tables."""

        self.database.execute(
            f"""
            CREATE TABLE IF NOT EXISTS
            {self.RESOURCE_TABLE} (
                resource_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                resource_type TEXT NOT NULL,
                category TEXT NOT NULL,
                status TEXT NOT NULL,
                ownership_type TEXT NOT NULL,

                owner_id TEXT,
                organization_id TEXT,
                business_id TEXT,
                customer_id TEXT,
                parent_resource_id TEXT,

                provider TEXT,
                region TEXT,
                location TEXT,
                hostname TEXT,
                ip_address TEXT,

                description TEXT,

                metadata TEXT NOT NULL DEFAULT '{{}}',
                tags TEXT NOT NULL DEFAULT '[]',

                created_at TEXT
                    DEFAULT CURRENT_TIMESTAMP,

                updated_at TEXT
                    DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        self.database.execute(
            f"""
            CREATE TABLE IF NOT EXISTS
            {self.RELATIONSHIP_TABLE} (
                relationship_id TEXT PRIMARY KEY,

                source_resource_id TEXT NOT NULL,

                target_resource_id TEXT NOT NULL,

                relationship_type TEXT NOT NULL,

                metadata TEXT NOT NULL DEFAULT '{{}}',

                created_at TEXT
                    DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

    # ==============================================================
    # RESOURCE CREATE
    # ==============================================================

    def create(
        self,
        resource: InfrastructureResource,
    ) -> InfrastructureResource:
        """Store an infrastructure resource."""

        self.initialize()

        self.database.execute(
            f"""
            INSERT INTO {self.RESOURCE_TABLE} (
                resource_id,
                name,
                resource_type,
                category,
                status,
                ownership_type,

                owner_id,
                organization_id,
                business_id,
                customer_id,
                parent_resource_id,

                provider,
                region,
                location,
                hostname,
                ip_address,

                description,
                metadata,
                tags
            )
            VALUES (
                ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?,
                ?, ?, ?
            )
            """,
            (
                resource.resource_id,
                resource.name,
                resource.resource_type.value,
                resource.category.value,
                resource.status.value,
                resource.ownership_type.value,

                resource.owner_id,
                resource.organization_id,
                resource.business_id,
                resource.customer_id,
                resource.parent_resource_id,

                resource.provider,
                resource.region,
                resource.location,
                resource.hostname,
                resource.ip_address,

                resource.description,

                json.dumps(
                    resource.metadata
                ),

                json.dumps(
                    resource.tags
                ),
            ),
        )

        return resource

    # ==============================================================
    # RESOURCE READ
    # ==============================================================

    def get(
        self,
        resource_id: str,
    ) -> Optional[InfrastructureResource]:
        """Return one infrastructure resource."""

        self.initialize()

        row = self.database.fetchone(
            f"""
            SELECT *
            FROM {self.RESOURCE_TABLE}
            WHERE resource_id = ?
            """,
            (resource_id,),
        )

        if row is None:
            return None

        return self._row_to_resource(row)

    # ==============================================================
    # RESOURCE LIST
    # ==============================================================

    def list_all(
        self,
    ) -> list[InfrastructureResource]:
        """Return all infrastructure resources."""

        self.initialize()

        rows = self.database.fetchall(
            f"""
            SELECT *
            FROM {self.RESOURCE_TABLE}
            ORDER BY created_at ASC
            """
        )

        return [
            self._row_to_resource(row)
            for row in rows
        ]

    # ==============================================================
    # RESOURCE DELETE
    # ==============================================================

    def delete(
        self,
        resource_id: str,
    ) -> bool:
        """Delete an infrastructure resource."""

        self.initialize()

        affected = self.database.execute(
            f"""
            DELETE FROM {self.RESOURCE_TABLE}
            WHERE resource_id = ?
            """,
            (resource_id,),
        )

        return affected > 0

    # ==============================================================
    # RELATIONSHIP CREATE
    # ==============================================================

    def create_relationship(
        self,
        relationship: InfrastructureRelationship,
    ) -> InfrastructureRelationship:
        """Store an infrastructure relationship."""

        self.initialize()

        self.database.execute(
            f"""
            INSERT INTO {self.RELATIONSHIP_TABLE} (
                relationship_id,
                source_resource_id,
                target_resource_id,
                relationship_type,
                metadata
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                relationship.relationship_id,

                relationship.source_resource_id,

                relationship.target_resource_id,

                relationship.relationship_type.value,

                json.dumps(
                    relationship.metadata
                ),
            ),
        )

        return relationship

    # ==============================================================
    # RELATIONSHIP LIST
    # ==============================================================

    def list_relationships(
        self,
    ) -> list[InfrastructureRelationship]:
        """Return all infrastructure relationships."""

        self.initialize()

        rows = self.database.fetchall(
            f"""
            SELECT *
            FROM {self.RELATIONSHIP_TABLE}
            ORDER BY created_at ASC
            """
        )

        return [
            self._row_to_relationship(row)
            for row in rows
        ]

    # ==============================================================
    # INTERNAL RESOURCE MAPPING
    # ==============================================================

    @staticmethod
    def _row_to_resource(
        row,
    ) -> InfrastructureResource:
        """Convert database row to resource model."""

        return InfrastructureResource(
            resource_id=row["resource_id"],

            name=row["name"],

            resource_type=(
                InfrastructureResourceType(
                    row["resource_type"]
                )
            ),

            category=(
                InfrastructureCategory(
                    row["category"]
                )
            ),

            status=(
                InfrastructureResourceStatus(
                    row["status"]
                )
            ),

            ownership_type=(
                InfrastructureOwnershipType(
                    row["ownership_type"]
                )
            ),

            owner_id=row["owner_id"],

            organization_id=(
                row["organization_id"]
            ),

            business_id=(
                row["business_id"]
            ),

            customer_id=(
                row["customer_id"]
            ),

            parent_resource_id=(
                row["parent_resource_id"]
            ),

            provider=row["provider"],

            region=row["region"],

            location=row["location"],

            hostname=row["hostname"],

            ip_address=row["ip_address"],

            description=row["description"],

            metadata=json.loads(
                row["metadata"] or "{}"
            ),

            tags=json.loads(
                row["tags"] or "[]"
            ),
        )

    # ==============================================================
    # INTERNAL RELATIONSHIP MAPPING
    # ==============================================================

    @staticmethod
    def _row_to_relationship(
        row,
    ) -> InfrastructureRelationship:
        """Convert database row to relationship model."""

        return InfrastructureRelationship(
            relationship_id=(
                row["relationship_id"]
            ),

            source_resource_id=(
                row["source_resource_id"]
            ),

            target_resource_id=(
                row["target_resource_id"]
            ),

            relationship_type=(
                InfrastructureRelationshipType(
                    row["relationship_type"]
                )
            ),

            metadata=json.loads(
                row["metadata"] or "{}"
            ),
        )


__all__ = [
    "InfrastructureRepository",
]
