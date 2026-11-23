# GLOBAL HOSPITALITY HOTELS RESORTS RESTAURANTS SERVICE WORK BUSINESS CORE ECOSYSTEM

**Parent:** GLOBAL BADA BUSINESS CORE ECOSYSTEM  
**ID:** `GLOBAL-HOSPITALITY-HOTELS-RESORTS-RESTAURANTS-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM`

Commercial services and work-business foundation for hotels, resorts, restaurants, accommodation operators, hospitality owners, suppliers and professional service providers.

## Architecture
- `domain_catalog.py`: service, work and commercial capability taxonomy.
- `policy.py`: provider, claims, privacy and authorization guardrails.
- `service.py`: read-only service catalog, filtering and readiness.
- `manager.py`: stable orchestration entry point and `get_manager()`.
- `manager.php`: PHP read-only facade.
- `ecosystem_manifest.json`: machine-readable scope and domain map.
- `tests/test_ecosystem.py`: deterministic contract tests.

## Service scope
Business strategy, operational improvement, revenue and marketing, distribution technology, procurement, staffing and training, finance/compliance coordination, property/asset support, franchise/investment readiness and India/global market expansion.

## Boundary
This module classifies and coordinates service capabilities. It does not itself provide licensed legal/accounting advice, issue permits, verify vendors, hire workers, process payroll, accept payments, execute bookings or guarantee investment outcomes. External integrations belong in the API/integration layer. Provider credentials and guest payment data must never be stored here.

## Coverage
Supports India and international market dimensions, including country, state/province, district/county, city and locality. Coverage is a model, not proof that every market/provider is onboarded.

**Readiness:** service taxonomy only; external service delivery and transactions remain disabled until separately implemented and verified.
