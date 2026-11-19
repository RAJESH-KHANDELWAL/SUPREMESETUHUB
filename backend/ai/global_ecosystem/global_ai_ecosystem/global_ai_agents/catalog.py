"""Read-only catalog of agent roles and reusable agent profiles."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

AGENT_CATALOG: dict[str, dict[str, Any]] = {
    "general_assistant": {
        "name": "General Assistant", "category": "assistant",
        "description": "Handles bounded multi-purpose user tasks and produces structured responses.",
        "capabilities": ["text", "reasoning", "research"], "tools": [],
        "memory_scope": "session", "approval_required": False, "status": "CATALOG_ONLY",
    },
    "research_analyst": {
        "name": "Research Analyst", "category": "research",
        "description": "Plans research, gathers evidence, evaluates sources and prepares cited findings.",
        "capabilities": ["research", "reasoning", "documents"],
        "tools": ["search", "document_reader"], "memory_scope": "project",
        "approval_required": False, "status": "CATALOG_ONLY",
    },
    "business_advisor": {
        "name": "Business Advisor", "category": "business",
        "description": "Analyzes business questions, options, risks, assumptions and measurable outcomes.",
        "capabilities": ["reasoning", "research", "documents"],
        "tools": ["search", "calculator", "document_reader"], "memory_scope": "project",
        "approval_required": False, "status": "CATALOG_ONLY",
    },
    "coding_assistant": {
        "name": "Coding Assistant", "category": "development",
        "description": "Reviews, explains, designs and proposes code changes within an assigned scope.",
        "capabilities": ["code", "reasoning"], "tools": ["repository_reader", "test_runner"],
        "memory_scope": "project", "approval_required": True, "status": "CATALOG_ONLY",
    },
    "document_agent": {
        "name": "Document Agent", "category": "documents",
        "description": "Processes document content, structures information and validates extracted fields.",
        "capabilities": ["documents", "text", "reasoning"], "tools": ["document_reader"],
        "memory_scope": "session", "approval_required": False, "status": "CATALOG_ONLY",
    },
    "workflow_coordinator": {
        "name": "Workflow Coordinator", "category": "orchestration",
        "description": "Prepares multi-agent task plans, dependencies, checkpoints and approval gates.",
        "capabilities": ["agents", "automation", "reasoning"], "tools": [],
        "memory_scope": "project", "approval_required": True, "status": "CATALOG_ONLY",
    },
}

def list_agents() -> list[dict[str, Any]]:
    return [{"id": key, **deepcopy(profile)} for key, profile in sorted(AGENT_CATALOG.items())]

def get_agent(agent_id: str) -> dict[str, Any]:
    key = agent_id.strip().lower()
    try:
        return {"id": key, **deepcopy(AGENT_CATALOG[key])}
    except KeyError as exc:
        raise KeyError("AI_AGENT_NOT_FOUND") from exc
