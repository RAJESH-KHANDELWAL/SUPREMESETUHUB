# GLOBAL AI AGENTS

**Package:** `backend/ai/global_ecosystem/global_ai_ecosystem/global_ai_agents/`  
**Parent:** `GLOBAL AI ECOSYSTEM`  
**Layer:** AI domain

## Responsibility

This package owns agent-domain definitions and contracts:

- Agent profiles and read-only catalog
- Agent request/result contracts
- Agent policy and approval requirements
- Tool capability contracts and allowlists
- Memory scope and retention policy descriptors
- Planning steps and dependency validation
- Explicit in-memory agent metadata registry
- Service boundary with injected executor

## Layer boundaries

| Layer | Owns |
|---|---|
| API | HTTP routes, authentication and transport schemas |
| AI / Agents | Agent identities, profiles, policies, plans and contracts |
| CORE | Application/business orchestration and cross-domain validation |
| ENGINE | Model/provider execution, tool dispatch and runtime lifecycle |

This package does not import API, CORE or ENGINE modules. It does not create
provider clients, read credentials, open databases, make network requests or
start autonomous loops. Execution is possible only through an explicitly
injected executor supplied by the composition root.

## Quick use

```python
from backend.ai.global_ecosystem.global_ai_ecosystem.global_ai_agents import (
    AgentRequest,
    GlobalAIAgentService,
    list_agents,
)

agents = list_agents()
service = GlobalAIAgentService()  # metadata-only until executor is injected
profile = service.describe("research_analyst")
```

## Status

`CATALOG_AND_CONTRACTS_READY` means the domain package and local contracts
exist. It does not mean an AI provider, model, tool or production runtime is
connected or operational.
