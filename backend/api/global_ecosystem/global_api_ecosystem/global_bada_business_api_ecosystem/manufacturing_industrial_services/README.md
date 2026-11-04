# Manufacturing, Industrial, Industries & Factory Services API Ecosystem

**Stable ID:** `manufacturing_industrial_services`  
**Canonical package:** `global_bada_business_api_ecosystem/manufacturing_industrial_services/`  
**Registry display name:** Manufacturing, Industrial, Industries & Factory Services  
**Coverage target:** India + Global  
**Channels:** Online, Offline and Hybrid  
**Implementation status:** Taxonomy/API scaffold

This package is maintained directly at the Bada Business API Ecosystem root. It is not stored under `industry_api_ecosystems/`.

## Scope

The taxonomy covers industrial manufacturing, factory setup and operations, production management, machinery and precision engineering, automotive and EV component manufacturing, electrical and electronics manufacturing, chemicals and materials processing, pharmaceutical and medical-product manufacturing, food and beverage processing, textile and technical-textile production, metal fabrication, packaging, automation, quality/testing, plant maintenance, factory utilities, environmental services, industrial safety and factory support services.

## API endpoints

Mounted under `/api/v1/global-ecosystem/business/industries/manufacturing-industrial-services`:

- `GET /status` — package status and taxonomy counts.
- `GET /integrity` — category/domain uniqueness and mapping integrity.
- `GET /categories` — list categories; optional `q` search.
- `GET /categories/{category_id}` — category detail.
- `GET /domains` — list business domains; optional `q` and `category_id` filters.
- `GET /domains/{domain_id}` — business-domain detail.

## Boundary with adjacent ecosystems

- Mining, mineral extraction, ore beneficiation and primary mineral-sector activity remain in `mining_metals_minerals`.
- Vehicle sales, dealerships, rentals, repair and mobility services remain in `automotive_mobility`; this package covers vehicle and component manufacturing.
- Fashion retail and consumer apparel commerce remain in `fashion_textiles_apparel`; this package covers industrial textile and garment production.
- Clinical healthcare, pharmacies and treatment remain in healthcare ecosystems; this package covers pharmaceutical and medical-device manufacturing.
- Restaurants, catering and food-service businesses remain in `food_hospitality_restaurants`; this package covers industrial food processing.
- Consumer electronics retail remains in `retail_ecommerce_consumer_goods`; this package covers electronics production.

## Data and compliance limits

This is a structured taxonomy, not a verified factory or supplier directory. It does not confirm factory existence, capacity, ownership, certifications, licences, environmental permissions, labour compliance, product quality, supplier availability, prices or live production status. Regulated manufacturing and safety obligations require jurisdiction-specific verification and qualified review before operational use.
