# Distribution Channels API Ecosystem

Independent, cross-industry API ecosystem for mapping how finished goods move from a manufacturer's dispatch point through commercial and fulfilment channels to business buyers and final customers.

**Package:** `distribution_channels_api_ecosystem`  
**Scope:** India + Global; online, offline and hybrid channels.  
**API prefix:** `/distribution-channels`

## Coverage

The taxonomy covers factory dispatch and finished-goods handling; company depots and warehouses; carrying & forwarding (C&F) agents; super stockists; national, regional, state and district distributors; authorized distributors; wholesalers and sub-wholesalers; stockists; dealers and sub-dealers; retailers and retail chains; franchise stores; B2B and B2C marketplaces; e-commerce and social-commerce sellers; D2C channels; institutional and bulk buyers; export/import channel partners; and final customer handover.

## Typical movement

Manufacturer dispatch → finished-goods warehouse / company depot → C&F agent or distribution centre → super stockist / distributor → wholesaler / dealer → retailer / marketplace seller → customer.

This is a reference flow, not a mandatory sequence. Direct-to-customer, institutional, tender, export and marketplace routes may bypass several intermediaries.

## Boundaries

- Manufacturing processes and production operations remain in the Manufacturing & Industrial Services ecosystem.
- Transport, freight, customs execution and logistics operations remain in their respective specialist ecosystems; this package represents channel hand-offs and integrations rather than duplicating those systems.
- Retail product categories and consumer storefront taxonomy remain in the Retail, E-commerce & Consumer Goods ecosystem.
- This package is a taxonomy/API scaffold, not a verified directory, live inventory feed, transaction platform or proof of provider availability.

## Package layout

All 25 channel modules are kept directly in this one package folder (there is no per-channel subfolder). Each channel module exposes its canonical record from `catalog.py`; the central catalogue remains the single source of truth.

Core files: `catalog.py`, `schemas.py`, `service.py`, `routes.py`, and `tests/test_service.py`.

## Business operating profiles

Each of the 25 channels now has a structured business profile served with its channel record:

- Business types and customer types
- Operating modes: online, offline and hybrid where relevant
- Revenue models
- Typical inbound sources and downstream hand-offs
- Core operating activities
- Typical business and transaction records
- Onboarding data fields

The profile is a discovery and data-modelling baseline. It does not assert that every business needs every listed document. Legal registrations, tax obligations, product licences, safety approvals, import/export permissions and standards depend on the actual activity, product, location, turnover and jurisdiction. Validate requirements against current official authorities before onboarding or operating.

## API response fields

`GET /distribution-channels/channels` and `GET /distribution-channels/channels/{channel_id}` include a `business_profile` object. The profile fields are descriptive taxonomies, not a live compliance checklist or provider verification.

The central `business_profiles.py` module is the single source of truth for these profile fields. Individual channel modules remain lightweight access points to the canonical catalogue and do not duplicate the profiles.
