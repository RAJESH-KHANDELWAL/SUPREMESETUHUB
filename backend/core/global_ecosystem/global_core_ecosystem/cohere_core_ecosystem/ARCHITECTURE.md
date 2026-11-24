# Cohere CORE architecture

Each capability folder owns its domain-specific contracts and orchestration entry point. Shared policies, models, schemas, lifecycle, events and security are centralized here.

CORE validates and describes work; it does not make network calls. API exposes transport, ENGINE executes provider requests and retries, DATABASE persists structured state, STORAGE handles files/artifacts, and PHP provides interoperability contracts. Never store provider credentials in source control.
