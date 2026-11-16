# GLOBAL AI CORE ECOSYSTEM

Provider-level control plane and canonical product Core inventory for the Bharat-to-global AI ecosystem. The runtime source of truth is `backend/global_ecosystem/global_ai_ecosystem/providers.py`; each registry entry has one dedicated `<provider_id>_core_ecosystem` package.

Every product package follows the Google Core ten-folder standard: authentication, capabilities, docs, events, lifecycle, models, schemas, security, services and tests. Root modules provide catalog, contracts, policy, shared product service, domain taxonomy, offering catalog, orchestration, manager status and PHP interoperability.

Legacy API aliases and 24 adjacent hosting/payment/advertising/content platform folders are preserved for compatibility and are not counted as canonical AI product packages. Frameworks, model families, inference routers and hosted API vendors retain their original runtime classifications.

CORE owns identity, capability metadata, policy, lifecycle, readiness and orchestration. API owns OAuth, secrets and transport. ENGINE owns inference and tools. No credentials are stored here; no live connection or API call is claimed.
