# Global Fashion, Textiles & Apparel API Ecosystem

**Canonical package:** `global_fashion_textiles_apparel_api_ecosystem/`

This is the single maintained implementation for Fashion, Textiles & Apparel across India and global markets. It classifies the value chain from textile fibres and yarns through manufacturing, processing, apparel design and production, retail, footwear and leather goods, home and technical textiles, fashion services, recycling, trade and sourcing.

## Package structure
- `catalog.py`: 12 categories and their subcategories
- `service.py`: category listing, search, detail lookup and status
- `schemas.py`: typed API response models
- `routes.py`: FastAPI endpoints
- `tests/`: service tests
- `__init__.py`: stable industry identity, coverage, channels and status

## API endpoints
- GET `/industries/fashion-textiles-apparel/status`
- GET `/industries/fashion-textiles-apparel/categories`
- GET `/industries/fashion-textiles-apparel/categories?q=...`
- GET `/industries/fashion-textiles-apparel/categories/{category_id}`

## Ownership and compatibility
This package is the canonical owner of fashion design, apparel, textiles, footwear, leather goods and fashion retail taxonomy. The former root-level `fashion_textiles_apparel/` and `industry_api_ecosystems/fashion_textiles_apparel/` paths are compatibility facades only; they must not contain duplicate implementations.

## Scope and limitations
Status is `taxonomy_scaffold`. India/global coverage and online/offline/hybrid channels are classification scopes, not proof of exhaustive coverage. This package does not verify live brands, factories, suppliers, product quality, textile certifications, licences or job vacancies.
