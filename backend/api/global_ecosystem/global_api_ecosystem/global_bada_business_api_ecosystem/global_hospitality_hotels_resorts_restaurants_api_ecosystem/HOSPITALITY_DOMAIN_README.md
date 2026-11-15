# Hotels, Resorts, Restaurants & Hospitality API Ecosystem

Stable legacy domain identifier: `food_hospitality_restaurants`.

## Scope
India and global taxonomy for hotels, resorts, restaurants, dhabas, cafes, bakeries, beverages served by hospitality businesses, catering, prepared-food delivery, accommodation, venues, institutional dining, restaurant procurement and restaurant technology.

## Food classification boundary
Food production, agricultural food supply chains, food processing, food testing, food hygiene and food-safety compliance are classified under `global_agriculture_food_natural_resources_api_ecosystem/`. The former `food_safety_quality` hospitality category has been moved to the Agriculture & Food ecosystem. Restaurant suppliers, commercial kitchens and food equipment remain here when they serve hospitality operators.

## Existing API
The maintained implementation remains in this directory. Preserve its Python package, catalog, routes, schemas, service and tests. The canonical root entry point is `global_hospitality_hotels_resorts_restaurants_api_ecosystem/`; the old root package remains a compatibility facade.

## Structure
Each active catalog category has its own directory and README under `categories/`. Shared directories cover jobs, businesses, India, global, coaches, consultants, advisors, API documentation and access tiers.

## Limitations
These folders are taxonomy/documentation scaffolds, not live hotel listings, restaurant listings, reservations, food-ordering systems, payment integrations or verified licences. Provider verification, FSSAI and other applicable local compliance, privacy, payments and production API integrations require separate implementation and testing.
