# GLOBAL BUSINESS API ECOSYSTEM

This package owns business-level workflows and shared business rules.

Core Python modules: `__init__.py`, `routes.py`, `service.py`, and `schemas.py`.

Companies, platforms, tools, services, and integrations are separate sibling GLOBAL API ECOSYSTEM packages under `global_api_ecosystem/`. Do not duplicate their registries or category entry points inside this business package. Business workflows may reference those central ecosystems through explicit interfaces.

Only add verified business metadata and integrations.