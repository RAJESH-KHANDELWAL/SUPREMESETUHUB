# Mining, Metals & Minerals API Ecosystem

**Canonical package location:** `global_bada_business_api_ecosystem/mining_metals_minerals/` (maintained directly at the Bada Business root, outside `industry_api_ecosystems/`).

This package provides a 12-category taxonomy and 20 business domains across mineral exploration, mining, processing, metal manufacturing, trade, equipment and mine environmental services.

## API endpoints
- GET `/industries/mining-metals-minerals/status`
- GET `/industries/mining-metals-minerals/categories`
- GET `/industries/mining-metals-minerals/categories?q=...`
- GET `/industries/mining-metals-minerals/categories/{category_id}`
- GET `/industries/mining-metals-minerals/domains`
- GET `/industries/mining-metals-minerals/domains?q=...&category_id=...`
- GET `/industries/mining-metals-minerals/domains/{domain_id}`

## Business-domain coverage
Iron ore; coal and lignite; gold and silver; copper; aluminium and bauxite; critical and rare-earth minerals; limestone and industrial minerals; quarrying and dimension stone; mineral exploration; drilling and blasting services; ore beneficiation; smelting and refining; iron and steel; non-ferrous metal products; mining equipment and technology; contract mining; mineral trading and exports; mineral transport and bulk handling; mine environment and rehabilitation; mine closure, safety and compliance services.

## Scope and limitations
This is a taxonomy/API scaffold, not live mineral reserve data, verified mining companies, mining leases, operating permits, supplier listings, job vacancies or environmental compliance certification. Mining, blasting, mineral processing, hazardous materials, exports and mine operations are subject to jurisdiction-specific laws, licenses and safety requirements. Verify authoritative records before publishing provider claims.
