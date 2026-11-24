# COHERE SHARED ORCHESTRATION

Read-only provider discovery and routing helpers.

- `CapabilityRegistry` exposes the canonical provider capability catalog.
- `CohereCoreManager` is the stable public manager facade.
- Provider discovery and dependency summaries are exposed by the root orchestrator.

This layer does not execute provider SDK calls, queue jobs, retries or scheduled work; those responsibilities belong to API/ENGINE.
