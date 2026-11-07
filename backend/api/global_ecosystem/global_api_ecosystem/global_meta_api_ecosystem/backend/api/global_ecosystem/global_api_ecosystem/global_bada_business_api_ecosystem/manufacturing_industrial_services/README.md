# Manufacturing, Industrial & Industries API Ecosystem

**Stable ID:** `manufacturing_industrial_services`  
**Canonical package:** `global_bada_business_api_ecosystem/manufacturing_industrial_services/`  
**Registry display name:** Manufacturing, Industrial & Industries  
**Coverage target:** India + Global  
**Channels:** Online, Offline and Hybrid  
**Implementation status:** Taxonomy/API scaffold

This package is maintained directly at the Bada Business API Ecosystem root, outside `industry_api_ecosystems/`.

## Scope

A broad industrial ecosystem covering manufacturing industries, industrial sectors and industrial operations, including:

- Discrete, process, heavy, light, precision and contract manufacturing.
- Automotive, EV, battery, aerospace-component and transportation-equipment manufacturing.
- Electrical, electronics, semiconductor, PCB and instrumentation industries.
- Chemical, petrochemical, polymer, pharmaceutical and medical-device manufacturing.
- Food processing, beverage production, agricultural processing and industrial biotechnology.
- Textile, technical textile, apparel production, leather and footwear manufacturing.
- Steel, metal, foundry, forging, fabrication, non-ferrous and advanced-material industries.
- Machinery, machine tools, capital equipment, industrial equipment and engineering.
- Packaging, printing, paper, glass, ceramics, cement and construction-material industries.
- Industrial automation, robotics, control systems, industrial IoT and smart manufacturing.
- Production planning, industrial engineering, quality systems, testing and metrology.
- Industrial infrastructure, plant engineering, utilities, maintenance and environmental systems.
- Factory setup, factory operations, industrial safety and factory services as supporting components—not the entire ecosystem.

## API endpoints

Mounted under `/api/v1/global-ecosystem/business/industries/manufacturing-industrial-services`:

- `GET /status` — package status and taxonomy counts.
- `GET /integrity` — category/domain uniqueness and mapping integrity.
- `GET /categories` — list categories; optional `q` search.
- `GET /categories/{category_id}` — category detail.
- `GET /domains` — list business domains; optional `q` and `category_id` filters.
- `GET /domains/{domain_id}` — business-domain detail.

## Boundary with adjacent ecosystems

- Mineral extraction, mining and primary ore activity remain in `mining_metals_minerals`; downstream industrial processing belongs here where applicable.
- Vehicle sales, dealerships, rentals, repair and mobility services remain in `automotive_mobility`; vehicle and component manufacturing belongs here.
- Fashion retail and consumer apparel commerce remain in `fashion_textiles_apparel`; textile and garment production belongs here.
- Clinical healthcare and patient treatment remain in healthcare ecosystems; pharmaceutical and medical-device manufacturing belongs here.
- Restaurants, catering and food-service businesses remain in `food_hospitality_restaurants`; industrial food processing belongs here.
- Consumer electronics retail remains in `retail_ecommerce_consumer_goods`; electronics production belongs here.

## Data and compliance limits

This is a structured taxonomy, not a verified factory, manufacturer, supplier or industrial-site directory. It does not confirm facility existence, capacity, ownership, certifications, licences, environmental permissions, labour compliance, product quality, supplier availability, prices or live production status. Regulated manufacturing and industrial safety obligations require jurisdiction-specific verification and qualified review.
