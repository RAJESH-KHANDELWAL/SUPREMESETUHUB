"""
MAIN BASE FOUNDATION
MASTER INFRASTRUCTURE RESOURCE MODEL

Central infrastructure resource definitions.

Supported resources include servers, VPS, cloud servers, networks, IPs, hosting, domains,
DNS, storage, databases, websites, WordPress, applications, containers, CDN, load balancers,
firewalls and backups.

This module defines data models only. It does not connect to providers or execute operations.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

class InfrastructureCategory(str, Enum):
    SERVER="server"; NETWORK="network"; STORAGE="storage"; DATABASE="database"
    HOSTING="hosting"; DOMAIN="domain"; WEBSITE="website"; APPLICATION="application"
    SECURITY="security"; DELIVERY="delivery"; BACKUP="backup"; OTHER="other"

class InfrastructureResourceType(str, Enum):
    DEDICATED_SERVER="dedicated_server"; VPS="vps"; CLOUD_SERVER="cloud_server"
    VIRTUAL_MACHINE="virtual_machine"; VPN="vpn"; NETWORK="network"; IP_ADDRESS="ip_address"
    DNS="dns"; STORAGE="storage"; OBJECT_STORAGE="object_storage"; DATABASE="database"
    DATABASE_SERVER="database_server"; HOSTING="hosting"; HOSTING_PLAN="hosting_plan"
    DOMAIN="domain"; WEBSITE="website"; WORDPRESS="wordpress"; APPLICATION="application"
    CONTAINER="container"; FIREWALL="firewall"; CDN="cdn"; LOAD_BALANCER="load_balancer"
    BACKUP="backup"; OTHER="other"

class InfrastructureResourceStatus(str, Enum):
    PROVISIONING="provisioning"; ACTIVE="active"; INACTIVE="inactive"; SUSPENDED="suspended"
    MAINTENANCE="maintenance"; FAILED="failed"; ARCHIVED="archived"; DELETED="deleted"

class InfrastructureOwnershipType(str, Enum):
    PLATFORM="platform"; ORGANIZATION="organization"; BUSINESS="business"; COMPANY="company"
    USER="user"; CUSTOMER="customer"; SHARED="shared"

@dataclass
class InfrastructureResource:
    resource_id: str
    name: str
    resource_type: InfrastructureResourceType
    category: InfrastructureCategory
    status: InfrastructureResourceStatus = InfrastructureResourceStatus.ACTIVE
    ownership_type: InfrastructureOwnershipType = InfrastructureOwnershipType.PLATFORM
    owner_id: Optional[str] = None
    organization_id: Optional[str] = None
    business_id: Optional[str] = None
    customer_id: Optional[str] = None
    parent_resource_id: Optional[str] = None
    provider: Optional[str] = None
    region: Optional[str] = None
    location: Optional[str] = None
    hostname: Optional[str] = None
    ip_address: Optional[str] = None
    description: Optional[str] = None
    metadata: dict = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "resource_id": self.resource_id, "name": self.name,
            "resource_type": self.resource_type.value, "category": self.category.value,
            "status": self.status.value, "ownership_type": self.ownership_type.value,
            "owner_id": self.owner_id, "organization_id": self.organization_id,
            "business_id": self.business_id, "customer_id": self.customer_id,
            "parent_resource_id": self.parent_resource_id, "provider": self.provider,
            "region": self.region, "location": self.location, "hostname": self.hostname,
            "ip_address": self.ip_address, "description": self.description,
            "metadata": dict(self.metadata), "tags": list(self.tags),
        }

class InfrastructureRelationshipType(str, Enum):
    CONTAINS="contains"; HOSTS="hosts"; RUNS_ON="runs_on"; CONNECTED_TO="connected_to"
    USES="uses"; DEPENDS_ON="depends_on"; SERVES="serves"; ROUTES_TO="routes_to"
    BACKS_UP="backs_up"; PROTECTED_BY="protected_by"; DELIVERED_BY="delivered_by"

@dataclass
class InfrastructureRelationship:
    relationship_id: str
    source_resource_id: str
    target_resource_id: str
    relationship_type: InfrastructureRelationshipType
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "relationship_id": self.relationship_id,
            "source_resource_id": self.source_resource_id,
            "target_resource_id": self.target_resource_id,
            "relationship_type": self.relationship_type.value,
            "metadata": dict(self.metadata),
        }

class InfrastructureRegistry:
    """In-memory registry for infrastructure resources."""
    def __init__(self) -> None:
        self.resources: dict[str, InfrastructureResource] = {}
        self.relationships: dict[str, InfrastructureRelationship] = {}

    def register(self, resource: InfrastructureResource) -> InfrastructureResource:
        self.resources[resource.resource_id] = resource
        return resource

    def get(self, resource_id: str) -> Optional[InfrastructureResource]:
        return self.resources.get(resource_id)

    def remove(self, resource_id: str) -> bool:
        if resource_id not in self.resources:
            return False
        del self.resources[resource_id]
        return True

    def list_all(self) -> list[InfrastructureResource]:
        return list(self.resources.values())

    def add_relationship(self, relationship: InfrastructureRelationship) -> InfrastructureRelationship:
        self.relationships[relationship.relationship_id] = relationship
        return relationship

    def get_relationship(self, relationship_id: str) -> Optional[InfrastructureRelationship]:
        return self.relationships.get(relationship_id)

    def list_relationships(self) -> list[InfrastructureRelationship]:
        return list(self.relationships.values())

    def list_children(self, resource_id: str) -> list[InfrastructureResource]:
        child_ids = {
            rel.target_resource_id for rel in self.relationships.values()
            if rel.source_resource_id == resource_id
            and rel.relationship_type in {
                InfrastructureRelationshipType.CONTAINS, InfrastructureRelationshipType.HOSTS
            }
        }
        return [item for item in self.resources.values() if item.resource_id in child_ids]

__all__ = [
    "InfrastructureCategory", "InfrastructureResourceType", "InfrastructureResourceStatus",
    "InfrastructureOwnershipType", "InfrastructureResource", "InfrastructureRelationshipType",
    "InfrastructureRelationship", "InfrastructureRegistry",
]
