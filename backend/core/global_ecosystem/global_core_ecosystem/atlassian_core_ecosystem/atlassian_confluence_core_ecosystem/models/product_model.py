"""Immutable metadata shape for Confluence."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ProductIdentity:
    ecosystem_id: str = "ATLASSIAN-CONFLUENCE-CORE-ECOSYSTEM"
    provider: str = "atlassian"
    display_name: str = "Confluence"
