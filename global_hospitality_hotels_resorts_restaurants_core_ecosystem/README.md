# GLOBAL HOSPITALITY HOTELS RESORTS RESTAURANTS CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**ID:** `GLOBAL-HOSPITALITY-HOTELS-RESORTS-RESTAURANTS-CORE-ECOSYSTEM`

Canonical industry core for accommodation, hotels, resorts, restaurants, food and beverage, guest experience, events, workforce, safety, sustainability and geographic coverage.

## Architecture
- `domain_catalog.py`: controlled industry domains and capabilities.
- `policy.py`: privacy, safety and authorization guardrails.
- `service.py`: read-only catalog access, lookup and search.
- `manager.py`: stable orchestration entry point and `get_manager()`.
- `manager.php`: PHP read-only facade.
- `ecosystem_manifest.json`: machine-readable identity and scope.
- `tests/test_ecosystem.py`: deterministic contract tests.

## Boundary
This is the industry-wide core, not the Bada Business services layer. API transport, booking/payment execution, external provider connectors and application workflows belong in their respective layers. Catalog entries do not establish provider verification, availability, price, licensing or compliance.

## Geography
Supports country, state/province, district/county, city and locality dimensions. India and international coverage must be populated and verified by downstream data sources.

## Guardrails
Minimize guest/employee personal data; never store passwords, access tokens or payment-card data here. Verify local food, fire, employment, accessibility, tax and licensing obligations before operations. High-impact actions require authentication, authorization and explicit consent.

**Readiness:** core taxonomy only; live operations are disabled.
