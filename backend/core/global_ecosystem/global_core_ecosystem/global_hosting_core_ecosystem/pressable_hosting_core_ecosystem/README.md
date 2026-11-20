# Provider Hosting Core Ecosystem

**Status:** `CORE_CATALOG_ONLY`

This provider package exposes identity, hosting capability metadata, discovery and readiness only. It does not call provider APIs, provision infrastructure, change DNS, deploy workloads or store credentials.

Files: `manager.py`, `manager.php`, `__init__.py`, `README.md`. Live integration requires a separately implemented API/Infrastructure adapter, authenticated configuration, authorization and successful smoke tests.
