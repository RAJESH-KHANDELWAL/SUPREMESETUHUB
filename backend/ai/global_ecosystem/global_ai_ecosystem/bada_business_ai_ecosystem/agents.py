"""Bada Business AI agent profiles; execution belongs to injected ENGINE adapters."""
from __future__ import annotations

BADA_BUSINESS_AGENTS = (
    {
        "id": "bb_business_advisor",
        "name": "Bada Business Advisor",
        "purpose": "Analyze business goals, constraints, risks and practical next steps.",
        "capabilities": ["business_learning", "business_research", "resource_understanding"],
        "approval_required": False,
    },
    {
        "id": "bb_program_guide",
        "name": "Bada Business Program Guide",
        "purpose": "Explain and compare programs using canonical catalog evidence.",
        "capabilities": ["resource_understanding", "program_comparison", "resource_recommendation"],
        "approval_required": False,
    },
    {
        "id": "bb_learning_coach",
        "name": "Bada Business Learning Coach",
        "purpose": "Turn business learning material into structured study plans and exercises.",
        "capabilities": ["business_learning", "business_content_analysis"],
        "approval_required": False,
    },
    {
        "id": "bb_research_analyst",
        "name": "Bada Business Research Analyst",
        "purpose": "Prepare evidence-led research briefs and identify information gaps.",
        "capabilities": ["business_research", "business_content_analysis"],
        "approval_required": False,
    },
    {
        "id": "bb_growth_analyst",
        "name": "Bada Business Growth Analyst",
        "purpose": "Analyze user-supplied campaign and business performance metrics.",
        "capabilities": ["performance_insights", "lead_qualification_support"],
        "approval_required": True,
    },
    {
        "id": "bb_resource_matcher",
        "name": "Bada Business Resource Matcher",
        "purpose": "Map user goals to relevant provider resources with transparent reasoning.",
        "capabilities": ["resource_recommendation", "program_comparison"],
        "approval_required": False,
    },
)


def list_bada_business_agents() -> list[dict]:
    return [dict(agent) for agent in BADA_BUSINESS_AGENTS]


def get_bada_business_agent(agent_id: str) -> dict:
    key = agent_id.strip().lower()
    for agent in BADA_BUSINESS_AGENTS:
        if agent["id"] == key:
            return dict(agent)
    raise KeyError("BADA_BUSINESS_AI_AGENT_NOT_FOUND")
