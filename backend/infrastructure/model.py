"""
MAIN BASE FOUNDATION
MASTER INFRASTRUCTURE RESOURCE MODEL

Central infrastructure resource definitions.

Supported resources:
- Dedicated Server
- VPS
- Cloud Server
- Virtual Machine
- VPN
- Network
- IP Address
- Hosting
- Domain
- DNS
- Storage
- Database
- Website
- WordPress
- Application
- Container
- CDN
- Load Balancer
- Firewall
- Backup

IMPORTANT:
This module defines infrastructure data models only.

It does NOT:
- connect to external providers
- create servers
- provision VPS
- register domains
- modify DNS
- execute hosting operations

Those responsibilities belong to their respective
service / engine / integration layers.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


# ==============================================================
# RESOURCE CATEGORY
# ==============================================================


class InfrastructureCategory(str, Enum):
    """High-level infrastructure resource categories."""

    SERVER = "server"
    NETWORK = "network"
    STORAGE = "storage"
    DATABASE = "database"
    HOSTING = "hosting"
    DOMAIN = "domain"
    WEBSITE = "website"
    APPLICATION = "application"
    SECURITY = "security"
    DELIVERY = "delivery"
    BACKUP = "backup"
    OTHER = "other"


# ==============================================================
# RESOURCE TYPE
# ==============================================================


class InfrastructureResourceType(str, Enum):
    """Concrete infrastructure resource types."""

    # SERVER
    DEDICATED_SERVER = "dedicated_server"
    VPS = "vps"
    CLOUD_SERVER = "cloud_server"
    VIRTUAL_MACHINE = "virtual_machine"

    # NETWORK
    VPN = "vpn"
    NETWORK = "network"
    IP_ADDRESS = "ip_address"
    DNS = "dns"

    # STORAGE
    STORAGE = "storage"
    OBJECT_STORAGE = "object_storage"

    # DATABASE
    DATABASE = "database"
    DATABASE_SERVER = "database_server"

    # HOSTING
    HOSTING = "hosting"
    HOSTING_PLAN = "hosting_plan"

    # DOMAIN / WEBSITE
    DOMAIN = "domain"
    WEBSITE = "website"

    # SOFTWARE
    WORDPRESS = "wordpress"
    APPLICATION = "application"
    CONTAINER = "container"

    # SECURITY
    FIREWALL = "firewall"

    # DELIVERY
    CDN = "cdn"
    LOAD_BALANCER = "load_balancer"

    # BACKUP
    BACKUP = "backup"

    OTHER = "other"


# ==============================================================
# RESOURCE STATUS
# ==============================================================


class InfrastructureResourceStatus(str, Enum):
    """Lifecycle status of infrastructure resources."""

    PROVISIONING = "provisioning"
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    MAINTENANCE = "maintenance"
    FAILED = "failed"
    ARCHIVED = "archived"
    DELETED = "deleted"


# ==============================================================
# OWNERSHIP TYPE
# ==============================================================


class InfrastructureOwnershipType(str, Enum):
    """Ownership / allocation relationship."""

    PLATFORM = "platform"
    ORGANIZATION = "organization"
    BUSINESS = "business"
    COMPANY = "company"
    USER = "user"
    CUSTOMER = "customer"
    SHARED = "shared"


# ==============================================================
# MASTER RESOURCE
# ==============================================================


@dataclass
class InfrastructureResource:
    """
    Master infrastructure resource record.

    This is a logical representation of a resource.

    Example:

        VPS
        Dedicated Server
        Hosting Plan
        Domain
        WordPress Site
        Database
        VPN
    """

    resource_id: str

    name: str

    resource_type: InfrastructureResourceType

    category: InfrastructureCategory

    status: InfrastructureResourceStatus = (
        InfrastructureResourceStatus.ACTIVE
    )

    ownership_type: InfrastructureOwnershipType = (
        InfrastructureOwnershipType.PLATFORM
    )

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

    metadata: dict = field(
        default_factory=dict
    )

    tags: list[str] = field(
        default_factory=list
    )

    def to_dict(self) -> dict:
        """Return resource information as a dictionary."""

        return {
            "resource_id": self.resource_id,

            "name": self.name,

            "resource_type": (
                self.resource_type.value
            ),

            "category": (
                self.category.value
            ),

            "status": (
                self.status.value
            ),

            "ownership_type": (
                self.ownership_type.value
            ),

            "owner_id": self.owner_id,

            "organization_id": (
                self.organization_id
            ),

            "business_id": (
                self.business_id
            ),

            "customer_id": (
                self.customer_id
            ),

            "parent_resource_id": (
                self.parent_resource_id
            ),

            "provider": self.provider,

            "region": self.region,

            "location": self.location,

            "hostname": self.hostname,

            "ip_address": self.ip_address,

            "description": self.description,

            "metadata": dict(self.metadata),

            "tags": list(self.tags),
        }


# ==============================================================
# RESOURCE RELATIONSHIP
# ==============================================================


class InfrastructureRelationshipType(str, Enum):
    """Relationships between infrastructure resources."""

    CONTAINS = "contains"

    HOSTS = "hosts"

    RUNS_ON = "runs_on"

    CONNECTED_TO = "connected_to"

    USES = "uses"

    DEPENDS_ON = "depends_on"

    SERVES = "serves"

    ROUTES_TO = "routes_to"

    BACKS_UP = "backs_up"

    PROTECTED_BY = "protected_by"

    DELIVERED_BY = "delivered_by"


@dataclass
class InfrastructureRelationship:
    """
    Relationship between two infrastructure resources.

    Example:

        Hosting
            HOSTS
        Website

        Website
            USES
        Domain

        Website
            RUNS_ON
        VPS
    """

    relationship_id: str

    source_resource_id: str

    target_resource_id: str

    relationship_type: InfrastructureRelationshipType

    metadata: dict = field(
        default_factory=dict
    )

    def to_dict(self) -> dict:
        """Return relationship data."""

        return {
            "relationship_id": (
                self.relationship_id
            ),

            "source_resource_id": (
                self.source_resource_id
            ),

            "target_resource_id": (
                self.target_resource_id
            ),

            "relationship_type": (
                self.relationship_type.value
            ),

            "metadata": dict(self.metadata),
        }


# ==============================================================
# RESOURCE REGISTRY
# ==============================================================


class InfrastructureRegistry:
    """
    In-memory registry for infrastructure resources.

    Database persistence will be handled separately.
    """

    def __init__(self) -> None:

        self.resources: dict[
            str,
            InfrastructureResource,
        ] = {}

        self.relationships: dict[
            str,
            InfrastructureRelationship,
        ] = {}

    # ----------------------------------------------------------
    # RESOURCE
    # ----------------------------------------------------------

    def register(
        self,
        resource: InfrastructureResource,
    ) -> InfrastructureResource:
        """Register a resource."""

        self.resources[
            resource.resource_id
        ] = resource

        return resource

    def get(
        self,
        resource_id: str,
    ) -> Optional[InfrastructureResource]:
        """Return a resource."""

        return self.resources.get(
            resource_id
        )

    def remove(
        self,
        resource_id: str,
    ) -> bool:
        """Remove a resource from the registry."""

        if resource_id not in self.resources:
            return False

        del self.resources[
            resource_id
        ]

        return True

    def list_all(
        self,
    ) -> list[InfrastructureResource]:
        """Return all resources."""

        return list(
            self.resources.values()
        )

    # ----------------------------------------------------------
    # RELATIONSHIPS
    # ----------------------------------------------------------

    def add_relationship(
        self,
        relationship: InfrastructureRelationship,
    ) -> InfrastructureRelationship:
        """Register a resource relationship."""

        self.relationships[
            relationship.relationship_id
        ] = relationship

        return relationship

    def get_relationship(
        self,
        relationship_id: str,
    ) -> Optional[InfrastructureRelationship]:
        """Return a relationship."""

        return self.relationships.get(
            relationship_id
        )

    def list_relationships(
        self,
    ) -> list[InfrastructureRelationship]:
        """Return all relationships."""

        return list(
            self.relationships.values()
        )

    def list_children(
        self,
        resource_id: str,
    ) -> list[InfrastructureResource]:
        """Return resources directly attached to a resource."""

        child_ids = {
            relationship.target_resource_id
            for relationship
            in self.relationships.values()
            if (
                relationship.source_resource_id
                == resource_id
                and relationship.relationship_type
                in {
                    InfrastructureRelationshipType.CONTAINS,
                    InfrastructureRelationshipType.HOSTS,
                }
            )
        }

        return [
            resource
            for resource in self.resources.values()
            if resource.resource_id
            in child_ids
        ]


__all__ = [
    "InfrastructureCategory",
    "InfrastructureResourceType",
    "InfrastructureResourceStatus",
    "InfrastructureOwnershipType",
    "InfrastructureResource",
    "InfrastructureRelationshipType",
    "InfrastructureRelationship",
    "InfrastructureRegistry",
]
