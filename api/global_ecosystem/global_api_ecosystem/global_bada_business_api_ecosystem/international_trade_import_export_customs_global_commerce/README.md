# International Trade, Import-Export, Customs & Global Commerce API Ecosystem

**Stable ID:** `international_trade_import_export_customs_global_commerce`  
**Canonical package:** `industry_api_ecosystems/international_trade_import_export_customs_global_commerce/`  
**Coverage target:** India + Global  
**Channels:** Online, Offline and Hybrid  
**Implementation status:** Taxonomy/API scaffold

A dedicated industry taxonomy for businesses and services that enable cross-border trade: importers, exporters, customs processes, trade documentation, market access, international sourcing, trade bodies and digital commerce.

## Scope

The 19 categories cover import-export businesses; international trade markets; customs clearance and brokers; trade documents and certificates; HS product classification; duties and tariffs; trade compliance; rules of origin and trade remedies; trade agreements; export promotion bodies; export incentives; global sourcing; buyer-seller networks; trade fairs and missions; cross-border e-commerce; trade intelligence; single-window facilitation; inspection and standards; and export consulting and capacity building.

## API endpoints

Mounted through the existing Bada Business industry API router:

- `GET /industries/international-trade-import-export/status`
- `GET /industries/international-trade-import-export/categories` — optional `q` and `channel` filters.
- `GET /industries/international-trade-import-export/categories/{category_id}`

## Boundaries with adjacent ecosystems

- General company structures, ownership forms, wholesale/retail business models and generic trade categories remain in `business_companies_trade_business_api_ecosystem`. This ecosystem focuses on the cross-border trade lifecycle and enabling services.
- Freight forwarding, shipping, ports as transport infrastructure, warehousing, cargo handling and delivery remain in Transport, Logistics & Supply Chain. Customs classification and clearance workflows are represented here; physical transport execution is not.
- Trade loans, letters of credit, foreign exchange, remittances, export credit insurance and payment execution remain in Finance, Banking & Insurance. This package may classify trade-finance referral/support touchpoints but does not provide financial products.
- Agriculture commodity trading and agri-specific export channels remain in the Agriculture, Food & Natural Resources ecosystem. This package covers cross-sector trade frameworks and generic import-export services.
- Domestic distribution, agents and channel partners remain in `distribution_channels_api_ecosystem`; cross-border importer/exporter and trade-partner discovery is classified here.
- Product manufacturing and factory operations remain in Manufacturing, Industrial & Industries.

## Data, legal and verification limits

This is a taxonomy/API scaffold, not a live customs portal, tariff engine, verified exporter directory, licensed customs-broker register, trade-finance service or legal advisory. HS classification, tariff rates, sanctions, export controls, licensing, origin rules and eligibility are jurisdiction- and date-sensitive and must be sourced from the relevant official authority before operational use. Do not infer a legal classification or customs duty from a category label. Provider credentials, buyer identities, certifications and trade enquiries require independent verification and provenance.
