# GLOBAL AI ECOSYSTEM

**Location:** `backend/ai/global_ecosystem/global_ai_ecosystem/`

This package is the backend's AI-domain ecosystem layer. It organizes AI
providers, model metadata, capabilities, services, agents, workflows,
knowledge/RAG components, infrastructure, governance controls and integrations.

## Layer boundaries

- **API:** HTTP transport, request/response contracts and route mounting. This
  package does not import or modify API modules.
- **AI:** provider/model/capability catalogs, agent definitions, ecosystem
  metadata, policy descriptors and orchestration contracts.
- **CORE:** application-level validation and business orchestration.
- **ENGINE:** actual runtime dispatch, model execution and provider execution.

The `global_ai_agents/` package owns generic agent profiles, request/result
contracts, tool allowlists, memory policy descriptors and planning metadata.
The `bada_business_ai_ecosystem/` package owns Bada Business-specific AI
capabilities, agent profiles, workflows, evidence policies and the read-only
adapter to the canonical Bada Business resource catalog.

No provider SDKs, API keys, network calls, database clients or runtime engines
are initialized by importing this package. Runtime execution is delegated only
through explicit dependency injection. The composition root is responsible
for wiring that boundary to the existing CORE/ENGINE path.

## Status semantics

- `CATALOG_ONLY`: metadata is known; no live connection is asserted.
- `NOT_CONFIGURED`: credentials or runtime adapter have not been verified.
- `REGISTERED`: a caller has explicitly registered an adapter.
- `READY`: a caller has explicitly marked an adapter ready after checks.

Catalog entries are descriptive, not proof of account access, subscription,
model availability, pricing, or live service health.

## Main modules

| Module | Responsibility |
|---|---|
| `catalog.py` | Unified read-only ecosystem catalog |
| `providers.py` / `models.py` | Provider and model metadata |
| `capabilities.py` / `services.py` | Capability and service taxonomy |
| `agents.py` / `workflows.py` | Shared agent components and workflow patterns |
| `global_ai_agents/` | Generic agent profiles, policies, contracts and planning |
| `bada_business_ai_ecosystem/` | Bada Business-specific AI capabilities, agents, workflows and resource adapter |
| `knowledge.py` | Ingestion, retrieval and RAG building blocks |
| `infrastructure.py` | Compute, serving and observability metadata |
| `governance.py` | Security, privacy, policy and cost controls |
| `integrations.py` | Integration descriptors |
| `schemas.py` | Typed metadata contracts |
| `registry.py` | In-memory, explicit provider registration boundary |
| `service.py` | Catalog queries and injected execution boundary |

## Quick use

```python
from backend.ai.global_ecosystem.global_ai_ecosystem import (
    BadaBusinessAIService,
    GlobalAIEcosystemService,
    get_catalog,
)
from backend.ai.global_ecosystem.global_ai_ecosystem.global_ai_agents import (
    GlobalAIAgentService,
    list_agents,
)

catalog = get_catalog()
service = GlobalAIEcosystemService()
agent_profiles = list_agents()
agent_service = GlobalAIAgentService()
bada_business_ai = BadaBusinessAIService()

# Runtime execution stays disabled until an executor is explicitly injected.
```

This is a structured foundation, not a claim that external AI providers,
models, tools or agent runtimes are already connected or operational.
