# Global Hotels, Resorts, Restaurants & Hospitality API Ecosystem

Canonical root-level entry point for hotels, resorts, restaurants, dhabas, cafes, bakeries, catering, food delivery, institutional dining, banquet venues and hospitality services across India and global markets.

The maintained implementation remains in `industry_api_ecosystems/food_hospitality_restaurants/`. This package exposes that implementation without duplicating its Python source.

## Classification boundary

- Food production, processing, agricultural food supply chains, food testing and food-safety compliance belong to `global_agriculture_food_natural_resources_api_ecosystem/`.
- Restaurants, dhabas, cafes, hotels, resorts, catering, prepared-food delivery, accommodation, event venues and restaurant operations belong here.
- Restaurant procurement, commercial kitchen equipment and restaurant POS/booking technology remain here because they directly support hospitality operators.

## Compatibility

The former root-level `food_hospitality_restaurants/` path remains a compatibility facade. Do not create a second implementation tree.

## Status

Taxonomy/API scaffold. This package does not imply verified businesses, live reservations, food ordering, payment processing, licences or provider integrations.
