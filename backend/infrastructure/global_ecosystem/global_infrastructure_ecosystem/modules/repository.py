"""Canonical infrastructure resource repository in Global Infrastructure Ecosystem."""
from __future__ import annotations
import json
from typing import Optional
from backend.database.service import DatabaseService
from backend.infrastructure.model import InfrastructureCategory, InfrastructureOwnershipType, InfrastructureRelationship, InfrastructureRelationshipType, InfrastructureResource, InfrastructureResourceStatus, InfrastructureResourceType

class InfrastructureRepository:
    RESOURCE_TABLE = "infrastructure_resources"
    RELATIONSHIP_TABLE = "infrastructure_relationships"

    def __init__(self, database_service: Optional[DatabaseService] = None):
        self.database = database_service or DatabaseService()

    def initialize(self) -> None:
        self.database.execute(f"""CREATE TABLE IF NOT EXISTS {self.RESOURCE_TABLE} (
            resource_id TEXT PRIMARY KEY, name TEXT NOT NULL, resource_type TEXT NOT NULL,
            category TEXT NOT NULL, status TEXT NOT NULL, ownership_type TEXT NOT NULL,
            owner_id TEXT, organization_id TEXT, business_id TEXT, customer_id TEXT,
            parent_resource_id TEXT, provider TEXT, region TEXT, location TEXT,
            hostname TEXT, ip_address TEXT, description TEXT,
            metadata TEXT NOT NULL DEFAULT '{{}}', tags TEXT NOT NULL DEFAULT '[]',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP, updated_at TEXT DEFAULT CURRENT_TIMESTAMP)""")
        self.database.execute(f"""CREATE TABLE IF NOT EXISTS {self.RELATIONSHIP_TABLE} (
            relationship_id TEXT PRIMARY KEY, source_resource_id TEXT NOT NULL,
            target_resource_id TEXT NOT NULL, relationship_type TEXT NOT NULL,
            metadata TEXT NOT NULL DEFAULT '{{}}', created_at TEXT DEFAULT CURRENT_TIMESTAMP)""")

    def create(self, resource: InfrastructureResource) -> InfrastructureResource:
        self.initialize()
        self.database.execute(f"""INSERT INTO {self.RESOURCE_TABLE} (
            resource_id,name,resource_type,category,status,ownership_type,owner_id,
            organization_id,business_id,customer_id,parent_resource_id,provider,region,
            location,hostname,ip_address,description,metadata,tags)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
            resource.resource_id, resource.name, resource.resource_type.value, resource.category.value,
            resource.status.value, resource.ownership_type.value, resource.owner_id,
            resource.organization_id, resource.business_id, resource.customer_id,
            resource.parent_resource_id, resource.provider, resource.region, resource.location,
            resource.hostname, resource.ip_address, resource.description,
            json.dumps(resource.metadata), json.dumps(resource.tags)))
        return resource

    def get(self, resource_id: str) -> Optional[InfrastructureResource]:
        self.initialize()
        row = self.database.fetchone(f"SELECT * FROM {self.RESOURCE_TABLE} WHERE resource_id = ?", (resource_id,))
        return self._row_to_resource(row) if row is not None else None

    def list_all(self) -> list[InfrastructureResource]:
        self.initialize()
        rows = self.database.fetchall(f"SELECT * FROM {self.RESOURCE_TABLE} ORDER BY created_at ASC")
        return [self._row_to_resource(row) for row in rows]

    def update(self, resource: InfrastructureResource) -> InfrastructureResource:
        self.initialize()
        cursor = self.database.execute(f"""UPDATE {self.RESOURCE_TABLE} SET
            name=?,resource_type=?,category=?,status=?,ownership_type=?,owner_id=?,
            organization_id=?,business_id=?,customer_id=?,parent_resource_id=?,provider=?,
            region=?,location=?,hostname=?,ip_address=?,description=?,metadata=?,tags=?,
            updated_at=CURRENT_TIMESTAMP WHERE resource_id=?""", (
            resource.name, resource.resource_type.value, resource.category.value, resource.status.value,
            resource.ownership_type.value, resource.owner_id, resource.organization_id,
            resource.business_id, resource.customer_id, resource.parent_resource_id,
            resource.provider, resource.region, resource.location, resource.hostname,
            resource.ip_address, resource.description, json.dumps(resource.metadata),
            json.dumps(resource.tags), resource.resource_id))
        if cursor.rowcount == 0:
            raise ValueError(f"Infrastructure resource not found: {resource.resource_id}")
        return resource

    def delete(self, resource_id: str) -> bool:
        self.initialize()
        cursor = self.database.execute(f"DELETE FROM {self.RESOURCE_TABLE} WHERE resource_id = ?", (resource_id,))
        return cursor.rowcount > 0

    def create_relationship(self, relationship: InfrastructureRelationship) -> InfrastructureRelationship:
        self.initialize()
        self.database.execute(f"""INSERT INTO {self.RELATIONSHIP_TABLE} (
            relationship_id,source_resource_id,target_resource_id,relationship_type,metadata)
            VALUES (?,?,?,?,?)""", (
            relationship.relationship_id, relationship.source_resource_id,
            relationship.target_resource_id, relationship.relationship_type.value,
            json.dumps(relationship.metadata)))
        return relationship

    def list_relationships(self) -> list[InfrastructureRelationship]:
        self.initialize()
        rows = self.database.fetchall(f"SELECT * FROM {self.RELATIONSHIP_TABLE} ORDER BY created_at ASC")
        return [self._row_to_relationship(row) for row in rows]

    @staticmethod
    def _row_to_resource(row) -> InfrastructureResource:
        return InfrastructureResource(
            resource_id=row["resource_id"], name=row["name"],
            resource_type=InfrastructureResourceType(row["resource_type"]),
            category=InfrastructureCategory(row["category"]),
            status=InfrastructureResourceStatus(row["status"]),
            ownership_type=InfrastructureOwnershipType(row["ownership_type"]),
            owner_id=row["owner_id"], organization_id=row["organization_id"],
            business_id=row["business_id"], customer_id=row["customer_id"],
            parent_resource_id=row["parent_resource_id"], provider=row["provider"],
            region=row["region"], location=row["location"], hostname=row["hostname"],
            ip_address=row["ip_address"], description=row["description"],
            metadata=json.loads(row["metadata"] or "{}"), tags=json.loads(row["tags"] or "[]"))

    @staticmethod
    def _row_to_relationship(row) -> InfrastructureRelationship:
        return InfrastructureRelationship(
            relationship_id=row["relationship_id"], source_resource_id=row["source_resource_id"],
            target_resource_id=row["target_resource_id"],
            relationship_type=InfrastructureRelationshipType(row["relationship_type"]),
            metadata=json.loads(row["metadata"] or "{}"))

__all__ = ["InfrastructureRepository"]
