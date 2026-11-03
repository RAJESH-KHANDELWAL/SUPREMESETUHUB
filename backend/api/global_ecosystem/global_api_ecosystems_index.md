# Global API Ecosystems

Standalone API ecosystem packages live directly under `global_api_ecosystem/`. They are separate from the Bada Business taxonomy tree.

## Standalone ecosystems
- `agriculture_food_natural_resources_api_ecosystem/` — Agriculture, food systems, allied industries and natural resources.
- `global_bada_business_api_ecosystem/` — Bada Business and its independent business vertical packages.

Each standalone package owns its taxonomy, models, service layer, schemas and routes. Register routers in the application only after integration tests and route-prefix checks.
