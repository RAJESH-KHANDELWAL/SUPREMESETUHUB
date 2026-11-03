# Global API Ecosystems

Standalone API ecosystem packages live directly under `global_api_ecosystem/`. The Bada Business ecosystem is a separate parent package that may contain its own business and service vertical packages, including healthcare when organized as a Bada Business vertical.

## Standalone ecosystems
- `agriculture_food_natural_resources_api_ecosystem/` — Agriculture, food systems, allied industries and natural resources.
- `global_bada_business_api_ecosystem/` — Bada Business and its business vertical packages. The healthcare package is nested inside this ecosystem.

Each package owns its taxonomy, models, service layer, schemas and routes. Register routers in the application only after integration tests and route-prefix checks.
