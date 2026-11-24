# Global Hospitality Hotels Resorts Restaurants Core Ecosystem

**Parent:** Global Core Ecosystem  
**Version:** 2.0.0  
**Mode:** Read-only industry foundation

## Scope
Canonical global taxonomy for accommodation, hotels, resorts, restaurants, food and beverage, guest experience, reservation distribution, property operations, events, workforce, revenue, safety, sustainability, technology, supply chains, accessibility and destination geography.

## Architecture
- `domain_catalog.py` — canonical domain taxonomy, lookup and search.
- `contracts.py` — stable identity, version and capability boundaries.
- `service.py` — read-only catalog service and readiness.
- `policy.py` — privacy and authorization guardrails.
- `manager.py` — stable orchestration entry point and singleton factory.
- `manager.php` — PHP manifest facade.
- `ecosystem_manifest.json` — machine-readable domain registry.
- `tests/test_ecosystem.py` — deterministic contract tests.

This is not a live booking engine, payment processor, PMS, OTA connector, verified provider directory or legal-compliance certification. No availability, licensing, quality or provider verification is implied. Never store credentials, payment-card data or unnecessary guest identity data in this package.
