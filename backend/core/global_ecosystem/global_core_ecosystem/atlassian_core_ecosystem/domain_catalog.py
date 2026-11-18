"""Atlassian Core domain taxonomy and coverage inventory."""
from __future__ import annotations
from typing import Any
from .product_catalog import list_atlassian_offerings

DOMAINS = [
    {
        "domain_id": "IDENTITY_AND_ORGANIZATION",
        "name": "Identity and Organization",
        "description": "Administration, directory, identity and organization-level policy metadata",
        "families": [
            "ADMIN-IDENTITY"
        ]
    },
    {
        "domain_id": "DEVELOPER_AND_SOURCE_CONTROL",
        "name": "Developer and Source Control",
        "description": "Repositories, pull requests and developer workflow metadata",
        "families": [
            "BITBUCKET",
            "JIRA"
        ]
    },
    {
        "domain_id": "KNOWLEDGE_AND_COLLABORATION",
        "name": "Knowledge and Collaboration",
        "description": "Spaces, pages and content lifecycle metadata",
        "families": [
            "CONFLUENCE"
        ]
    },
    {
        "domain_id": "WORK_MANAGEMENT_AND_PLANNING",
        "name": "Work Management and Planning",
        "description": "Projects, issues, boards, sprints and service request coordination",
        "families": [
            "JIRA",
            "JIRA-SERVICE-MANAGEMENT"
        ]
    },
    {
        "domain_id": "IT_SERVICE_AND_OPERATIONS",
        "name": "IT Service and Operations",
        "description": "Service projects, incidents, requests, changes and service-level metadata",
        "families": [
            "JIRA-SERVICE-MANAGEMENT"
        ]
    },
    {
        "domain_id": "GOVERNANCE_AND_SECURITY",
        "name": "Governance and Security",
        "description": "Access, permissions, provisioning and policy boundaries",
        "families": [
            "ADMIN-IDENTITY",
            "BITBUCKET",
            "CONFLUENCE"
        ]
    }
]

def list_atlassian_domain_inventory() -> list[dict[str, Any]]:
    offerings = list_atlassian_offerings()
    return [{**domain, "offering_count": sum(1 for item in offerings if domain["domain_id"] in item["domains"])} for domain in DOMAINS]

def atlassian_domain_summary() -> dict[str, Any]:
    inventory = list_atlassian_domain_inventory()
    return {"success": True, "domain_count": len(inventory), "offering_count": len(list_atlassian_offerings()), "live_connections_verified": 0, "domains": inventory}
