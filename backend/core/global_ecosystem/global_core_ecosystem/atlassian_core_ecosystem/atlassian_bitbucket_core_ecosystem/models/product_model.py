"""Immutable metadata shape for Bitbucket."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ProductIdentity:
    ecosystem_id: str = "ATLASSIAN-BITBUCKET-CORE-ECOSYSTEM"
    provider: str = "atlassian"
    display_name: str = "Bitbucket"
