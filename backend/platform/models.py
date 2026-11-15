"""
MAIN BASE FOUNDATION
PLATFORM MODELS

MASTER PLATFORM MODEL

Supports:
- Social platforms
- Profiles
- Pages
- Channels
- Communities
- Groups
- Business profiles
- Company profiles
- Creator profiles

This layer describes platform resources.

Authorization, database, API, engine,
domain and hosting logic remain separate.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


# ==============================================================
# PLATFORM TYPE
# ==============================================================


class PlatformType(str, Enum):
    """Types of platforms supported by MAIN BASE FOUNDATION."""

    SOCIAL = "social"
    MESSAGING = "messaging"
    PROFESSIONAL = "professional"
    VIDEO = "video"
    COMMUNITY = "community"
    CONTENT = "content"
    BUSINESS = "business"
    DIGITAL = "digital"
    OTHER = "other"


# ==============================================================
# PLATFORM PROVIDER
# ==============================================================


class PlatformProvider(str, Enum):
    """Known external-style platform categories."""

    INSTAGRAM = "instagram"
    FACEBOOK = "facebook"
    WHATSAPP = "whatsapp"
    LINKEDIN = "linkedin"
    YOUTUBE = "youtube"
    REDDIT = "reddit"
    X = "x"
    THREADS = "threads"

    DISCORD = "discord"
    QUORA = "quora"
    PINTEREST = "pinterest"
    TIKTOK = "tiktok"
    TWITCH = "twitch"
    MEDIUM = "medium"

    WECHAT = "wechat"
    LINE = "line"

    CUSTOM = "custom"


# ==============================================================
# PLATFORM OBJECT
# ==============================================================


class PlatformObjectType(str, Enum):
    """Objects that can exist inside a platform."""

    PROFILE = "profile"

    PAGE = "page"

    CHANNEL = "channel"

    COMMUNITY = "community"

    GROUP = "group"

    BUSINESS_PROFILE = "business_profile"

    COMPANY_PROFILE = "company_profile"

    CREATOR_PROFILE = "creator_profile"

    ORGANIZATION_PROFILE = "organization_profile"

    WEBSITE = "website"

    APP = "app"

    OTHER = "other"


# ==============================================================
# RESOURCE STATUS
# ==============================================================


class PlatformResourceStatus(str, Enum):
    """Lifecycle status of a platform resource."""

    ACTIVE = "active"

    INACTIVE = "inactive"

    SUSPENDED = "suspended"

    ARCHIVED = "archived"

    DELETED = "deleted"


# ==============================================================
# PLATFORM
# ==============================================================


@dataclass
class Platform:
    """
    Represent a platform available inside the ecosystem.

    Example:
        Instagram
        YouTube
        WhatsApp
        LinkedIn
        Reddit
        Custom platform
    """

    platform_id: str

    name: str

    platform_type: PlatformType

    provider: PlatformProvider = (
        PlatformProvider.CUSTOM
    )

    description: Optional[str] = None

    icon: Optional[str] = None

    keywords: list[str] = field(
        default_factory=list
    )

    active: bool = True

    metadata: dict = field(
        default_factory=dict
    )

    def to_dict(self) -> dict:
        """Return platform information."""

        return {
            "platform_id": self.platform_id,
            "name": self.name,
            "platform_type": (
                self.platform_type.value
            ),
            "provider": (
                self.provider.value
            ),
            "description": self.description,
            "icon": self.icon,
            "keywords": list(self.keywords),
            "active": self.active,
            "metadata": dict(self.metadata),
        }


# ==============================================================
# PLATFORM RESOURCE
# ==============================================================


@dataclass
class PlatformResource:
    """
    Represent an object/resource inside a platform.

    Examples:
        Instagram Profile
        Facebook Page
        WhatsApp Community
        LinkedIn Company Page
        YouTube Channel
        Reddit Community
    """

    resource_id: str

    platform_id: str

    name: str

    object_type: PlatformObjectType

    owner_id: Optional[str] = None

    organization_id: Optional[str] = None

    parent_resource_id: Optional[str] = None

    status: PlatformResourceStatus = (
        PlatformResourceStatus.ACTIVE
    )

    username: Optional[str] = None

    slug: Optional[str] = None

    description: Optional[str] = None

    icon: Optional[str] = None

    keywords: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

    def to_dict(self) -> dict:
        """Return platform resource data."""

        return {
            "resource_id": self.resource_id,

            "platform_id": self.platform_id,

            "name": self.name,

            "object_type": (
                self.object_type.value
            ),

            "owner_id": self.owner_id,

            "organization_id": (
                self.organization_id
            ),

            "parent_resource_id": (
                self.parent_resource_id
            ),

            "status": self.status.value,

            "username": self.username,

            "slug": self.slug,

            "description": self.description,

            "icon": self.icon,

            "keywords": list(self.keywords),

            "metadata": dict(self.metadata),
        }


# ==============================================================
# PLATFORM REGISTRY
# ==============================================================


class PlatformRegistry:
    """
    Registry for platform definitions.

    This does not perform authentication
    or external API communication.
    """

    def __init__(self) -> None:

        self.platforms: dict[
            str,
            Platform,
        ] = {}

    def register(
        self,
        platform: Platform,
    ) -> Platform:
        """Register a platform."""

        self.platforms[
            platform.platform_id
        ] = platform

        return platform

    def get(
        self,
        platform_id: str,
    ) -> Optional[Platform]:
        """Return a platform by ID."""

        return self.platforms.get(
            platform_id
        )

    def remove(
        self,
        platform_id: str,
    ) -> bool:
        """Remove a platform definition."""

        if platform_id not in self.platforms:
            return False

        del self.platforms[
            platform_id
        ]

        return True

    def list_all(self) -> list[Platform]:
        """Return all registered platforms."""

        return list(
            self.platforms.values()
        )


# ==============================================================
# RESOURCE REGISTRY
# ==============================================================


class PlatformResourceRegistry:
    """
    Registry for profiles, pages, channels,
    communities, groups and other platform resources.
    """

    def __init__(self) -> None:

        self.resources: dict[
            str,
            PlatformResource,
        ] = {}

    def register(
        self,
        resource: PlatformResource,
    ) -> PlatformResource:
        """Register a platform resource."""

        self.resources[
            resource.resource_id
        ] = resource

        return resource

    def get(
        self,
        resource_id: str,
    ) -> Optional[PlatformResource]:
        """Return a resource by ID."""

        return self.resources.get(
            resource_id
        )

    def remove(
        self,
        resource_id: str,
    ) -> bool:
        """Remove a resource."""

        if resource_id not in self.resources:
            return False

        del self.resources[
            resource_id
        ]

        return True

    def list_all(
        self,
    ) -> list[PlatformResource]:
        """Return all platform resources."""

        return list(
            self.resources.values()
        )

    def list_by_platform(
        self,
        platform_id: str,
    ) -> list[PlatformResource]:
        """Return resources belonging to a platform."""

        return [
            resource
            for resource in self.resources.values()
            if resource.platform_id
            == platform_id
        ]

    def list_by_owner(
        self,
        owner_id: str,
    ) -> list[PlatformResource]:
        """Return resources belonging to an owner."""

        return [
            resource
            for resource in self.resources.values()
            if resource.owner_id
            == owner_id
        ]

    def list_by_organization(
        self,
        organization_id: str,
    ) -> list[PlatformResource]:
        """Return resources belonging to an organization."""

        return [
            resource
            for resource in self.resources.values()
            if resource.organization_id
            == organization_id
        ]


__all__ = [
    "PlatformType",
    "PlatformProvider",
    "PlatformObjectType",
    "PlatformResourceStatus",
    "Platform",
    "PlatformResource",
    "PlatformRegistry",
    "PlatformResourceRegistry",
]
