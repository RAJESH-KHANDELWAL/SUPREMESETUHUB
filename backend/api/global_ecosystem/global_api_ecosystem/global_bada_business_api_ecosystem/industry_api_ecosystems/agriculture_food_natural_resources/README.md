# Agriculture, Food & Natural Resources API

Domain package within `industry_api_ecosystems`.

## Included taxonomy

The catalog defines 16 top-level categories covering crop farming, horticulture, organic and regenerative agriculture, livestock and dairy, fisheries, forestry, agri-inputs, machinery, irrigation, food processing and manufacturing, food safety/testing/compliance, cold chain, markets and trade, agri-tech, rural finance, and bioenergy.

## Food safety and compliance

This is the canonical category for food hygiene and sanitation, food testing laboratories, quality audits, food safety training, traceability, standards, certification, licensing and regulatory compliance. Restaurant-specific procurement, commercial kitchen equipment and hospitality operations remain in the hospitality ecosystem.

## Endpoints

Mounted under the Industry API router:
- `GET /industries/agriculture-food-natural-resources/status`
- `GET /industries/agriculture-food-natural-resources/categories`
- `GET /industries/agriculture-food-natural-resources/categories?q=dairy`
- `GET /industries/agriculture-food-natural-resources/categories/{category_id}`

This is a structured taxonomy, not a live directory of farms, suppliers, buyers, prices, inventory, licences or government schemes. No third-party API integration or regulatory approval is implied.
