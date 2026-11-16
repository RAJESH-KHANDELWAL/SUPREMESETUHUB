# GOOGLE CLOUD CORE ECOSYSTEM

**Parent:** GLOBAL CLOUD CORE ECOSYSTEM  
**Canonical provider ID:** `google_cloud`  
**Runtime source:** `backend/global_ecosystem/global_cloud_ecosystem/catalog.py`

This package is the reference layout for provider-specific Cloud Core packages. It owns Google Cloud provider identity, cloud capability metadata, region/scope declarations, lifecycle/readiness metadata and security policy contracts.

It does not implement Google Cloud authentication, service-account key handling, SDK clients, resource provisioning, billing operations, storage transfers, VM operations, Kubernetes operations or data persistence. Those belong to API, Engine, Database, Storage and Infrastructure layers.

The canonical provider identity is `google_cloud`. Google Cloud regions and individual products/services are not separate provider identities in this catalog.

The ten responsibility folders are documented in their local README files. Empty scaffolds are not production integrations. Provider presence in the catalog does not prove an active Google Cloud account or live API connectivity.
