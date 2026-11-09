# GLOBAL AI ECOSYSTEM

**Location:** `backend/ai/global_ecosystem/global_ai_ecosystem/`

This package is the backend's AI-domain ecosystem layer. It organizes AI
providers, model metadata, capabilities, services, agents, workflows,
knowledge/RAG components, infrastructure, governance controls and integrations.

## Layer boundaries

- **API:** HTTP transport, request/response contracts and route mounting. This
  package does not import or modify API modules.
- **AI:** provider/model/capability catalog, ecosystem metadata, policy
  descriptors and orchestration contracts. This package lives here.
- **CORE:** application-level validation and business orchestration.
- **ENGINE:** actual runtime dispatch and provider execution.

No provider SDKs, API keys, network calls, database clients or runtime engines
are initialized by importing this package. The service accepts an executor
through dependency injection; the composition root is responsible for wiring
it to the existing CORE/ENGINE path.

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
| `agents.py` / `workflows.py` | Agent and workflow contracts |
| `knowledge.py` | Ingestion, retrieval and RAG building blocks |
| `infrastructure.py` | Compute, serving and observability metadata |
| `governance.py` | Security, privacy, policy and cost controls |
| `integrations.py` | Integration descriptors |
| `schemas.py` | Typed metadata contracts |
| `registry.py` | In-memory, explicit registration boundary |
| `service.py` | Catalog queries and injected execution boundary |

## Quick use

```python
from backend.ai.global_ecosystem.global_ai_ecosystem import (
    GlobalAIEcosystemService,
    get_catalog,
)

catalog = get_catalog()
service = GlobalAIEcosystemService()
summary = service.status()

# Runtime execution is disabled until an executor is explicitly injected.
```

This is a structured foundation, not a claim that external AI providers are
already connected or that live generation has been enabled.
