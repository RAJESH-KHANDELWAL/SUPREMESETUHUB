# GLOBAL BADA BUSINESS ECOSYSTEM

Canonical global namespace: `backend/global_ecosystem/global_bada_business_ecosystem/`

This namespace indexes the Bada Business and direct-selling business families
within SUPREMESETUHUB. It owns ecosystem identity and navigation only.

## Ecosystem hierarchy

```text
GLOBAL BADA BUSINESS ECOSYSTEM
└── GLOBAL NETWORK MARKETING & DIRECT SELLING BUSINESS ECOSYSTEM
    ├── YOUTAG WELLNESS ECOSYSTEM
    └── YOUTAG RECHARGES ECOSYSTEM
```

### GLOBAL NETWORK MARKETING & DIRECT SELLING BUSINESS ECOSYSTEM

This category groups network marketing, direct selling, distributor/dealer,
referral, product-promotion and recharge-business domains.

Child namespaces:

- `global_youtag_wellness_ecosystem/` — YOUTAG WELLNESS business/product
  ecosystem namespace.
- `global_youtag_recharges_ecosystem/` — YOUTAG RECHARGES services and
  recharge-business namespace.

The two YOUTAG child ecosystems are separate business domains. They must not
be treated as the same product, service, catalog, or transaction flow.

## Architecture boundaries

- This directory owns the global ecosystem namespace and its documentation/index.
- CORE owns canonical business identities and lifecycle rules.
- API owns HTTP contracts and integration endpoints.
- ENGINE owns orchestration and business workflows.
- DATABASE owns persistence and schema.
- Authentication, credentials, account access, payments, and live provider
  connections remain in their separately owned layers.
- Do not copy or relocate existing implementations into this namespace.
- Namespace presence does not mean a service, provider, account connection,
  product catalog, recharge transaction, or dataset is implemented or verified.

## Existing Bada Business resources

Canonical Bada Business resources remain in
`backend/bada_business_ecosystem/`. API implementation remains in
`backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`.

This global namespace is an index/ownership marker only. Keep canonical catalogs,
API routes, CORE, ENGINE, DATABASE, authentication, and runtime implementations
in their respective layers.

## YOUTAG integration status

The YOUTAG Wellness and YOUTAG Recharges entries here define ecosystem
boundaries only. They do not assert verified official APIs, account
authentication, live connectivity, payment processing, recharge execution,
or transaction status. Those capabilities require separately verified
provider documentation, credentials, contracts, and tests.
