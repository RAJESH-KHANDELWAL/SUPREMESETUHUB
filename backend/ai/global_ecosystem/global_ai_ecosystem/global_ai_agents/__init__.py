"""GLOBAL AI AGENTS domain package.

Owns agent definitions, profiles, policies, tool contracts, memory contracts,
planning metadata and lifecycle descriptors. It does not execute models, call
providers, expose HTTP routes or implement CORE/ENGINE responsibilities.
"""
from .catalog import AGENT_CATALOG, get_agent, list_agents
from .contracts import AgentRequest, AgentResult
from .policies import DEFAULT_AGENT_POLICY
from .registry import AgentRegistry
from .service import GlobalAIAgentService

LAYER = "AI"
ECOSYSTEM_ID = "GLOBAL_AI_ECOSYSTEM"
PACKAGE_ID = "GLOBAL_AI_AGENTS"
STATUS = "CATALOG_AND_CONTRACTS_READY"

__all__ = [
    "AGENT_CATALOG", "AgentRegistry", "AgentRequest", "AgentResult",
    "DEFAULT_AGENT_POLICY", "GlobalAIAgentService", "get_agent",
    "list_agents", "LAYER", "ECOSYSTEM_ID", "PACKAGE_ID", "STATUS",
]
