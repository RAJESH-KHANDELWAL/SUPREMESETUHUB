"""Immutable metadata shape for Atlassian Administration and Identity."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ProductIdentity:
    ecosystem_id: str = "ATLASSIAN-ADMIN-IDENTITY-CORE-ECOSYSTEM"
    provider: str = "atlassian"
    display_name: str = "Atlassian Administration and Identity"
