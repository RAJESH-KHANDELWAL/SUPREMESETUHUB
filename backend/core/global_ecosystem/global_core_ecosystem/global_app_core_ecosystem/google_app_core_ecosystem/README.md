# GOOGLE APP CORE ECOSYSTEM

**Parent:** GLOBAL APP CORE ECOSYSTEM  
**Canonical provider ID:** `google`  
**Runtime source:** `backend/global_ecosystem/global_app_ecosystem/providers.py`

This package is the reference implementation layout for provider-specific App Core packages. Its responsibility is Google application-provider identity, product/app classification, declared capability metadata, lifecycle/readiness metadata and security boundaries.

It does not implement Google OAuth, API clients, API calls, account access, Drive/Gmail/Maps operations, app installation or data persistence. Those belong to the API, Engine, Database and Storage layers.

All provider metadata must be resolved from canonical provider ID `google`; product names such as Android, Gmail, Maps, Drive, Photos, Workspace and Play Store are application examples, not separate provider identities in this catalog.

The ten responsibility folders are documented in their local README files. Empty scaffolds are not production integrations.
