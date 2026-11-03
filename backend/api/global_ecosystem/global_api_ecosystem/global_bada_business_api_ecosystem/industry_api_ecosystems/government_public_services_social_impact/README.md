# Government, Public Services & Social Impact API Ecosystem

Unified canonical API ecosystem for public-sector services, citizen services, nonprofits and social-impact organizations. Related taxonomies are organized as category folders under `categories/`; the retired parallel package delegates here.

- Coverage: India and global
- Channels: online, offline and hybrid
- Categories: 14
- Status: `taxonomy_scaffold`

## API endpoints

- `GET /industries/government-public-services-social-impact/status`
- `GET /industries/government-public-services-social-impact/categories`
- `GET /industries/government-public-services-social-impact/categories?q=...`
- `GET /industries/government-public-services-social-impact/categories/{category_id}`

## Structure

Each category has its own folder with `__init__.py` and `README.md`. Shared API routing, schemas, service logic and catalog remain at ecosystem root.

## Data boundaries

This is a discovery taxonomy only. It does not assert live listings, government endorsement, provider verification, professional licensing, regulatory approval or quality certification. Integrations and verification workflows must be implemented separately. Keep stable legacy identifiers mapped through `LEGACY_CATEGORY_CROSSWALK`.
