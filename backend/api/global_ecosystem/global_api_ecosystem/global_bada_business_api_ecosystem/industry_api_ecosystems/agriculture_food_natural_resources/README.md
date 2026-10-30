# Agriculture, Food & Natural Resources API

Domain package within `industry_api_ecosystems`.

## Included taxonomy

The catalog currently defines 15 top-level categories covering crop farming, horticulture, organic and regenerative agriculture, livestock and dairy, fisheries, forestry, agri-inputs, machinery, irrigation, food processing, cold chain, markets and trade, agri-tech, rural finance, and bioenergy.

## Endpoints

Mounted under the Industry API router:
- `GET /industries/agriculture-food-natural-resources/status`
- `GET /industries/agriculture-food-natural-resources/categories`
- `GET /industries/agriculture-food-natural-resources/categories?q=dairy`
- `GET /industries/agriculture-food-natural-resources/categories/{category_id}`

## Scope and limitations

This is a structured taxonomy, not a live directory of farms, suppliers, buyers, prices, inventory, or government schemes. No third-party API integration is claimed. Future data connectors require official documentation, licensing/permissions, authentication, rate-limit handling, validation, and tests. Country-specific regulatory and food-safety requirements must be reviewed before enabling transactions or advice.
