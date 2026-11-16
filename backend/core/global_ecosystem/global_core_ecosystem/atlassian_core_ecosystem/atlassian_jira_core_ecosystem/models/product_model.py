"""Immutable metadata shape for Jira."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ProductIdentity:
    ecosystem_id: str = "ATLASSIAN-JIRA-CORE-ECOSYSTEM"
    provider: str = "atlassian"
    display_name: str = "Jira"
