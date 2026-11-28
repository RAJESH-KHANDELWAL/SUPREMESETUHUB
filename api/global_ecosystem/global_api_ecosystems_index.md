# Global API Ecosystems

Standalone API ecosystem packages live directly under `global_api_ecosystem/`. The Bada Business ecosystem is a separate parent package that may contain its own business and service vertical packages, including healthcare when organized as a Bada Business vertical.

## Standalone ecosystems
- `global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_api_ecosystem/` — dedicated cultural knowledge API for Vasudhaiva Kutumbakam, Sanatan Dharma, Bharat Sanskriti, heritage and world cultures.
- `global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_api_ecosystem/` — separate API for cultural services, cultural work, and culture-based business capabilities; it is not nested under Bada Business.
- `global_bada_business_api_ecosystem/global_agriculture_food_natural_resources_api_ecosystem/` — Central Agriculture, Food & Natural Resources ecosystem under Global Bada Business.
- `global_bada_business_api_ecosystem/` — Bada Business and its business vertical packages. The healthcare package is nested inside this ecosystem.

Each package owns its taxonomy, models, service layer, schemas and routes. Register routers in the application only after integration tests and route-prefix checks.
