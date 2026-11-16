"""Immutable metadata shape for Jira Service Management."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ProductIdentity:
    ecosystem_id: str = "ATLASSIAN-JIRA-SERVICE-MANAGEMENT-CORE-ECOSYSTEM"
    provider: str = "atlassian"
    display_name: str = "Jira Service Management"
