# GLOBAL YOUTAG BUSINESS ECOSYSTEM

Parent: `GLOBAL NETWORK MARKETING & DIRECT SELLING BUSINESS ECOSYSTEM`

YOUTAG is represented here as **one business/company ecosystem**. YOUTAG WELLNESS and YOUTAG RECHARGES are two separate apps/platforms operated within that same YOUTAG business ecosystem. They are not separate companies or independent business ecosystems.

## Application structure

```text
GLOBAL YOUTAG BUSINESS ECOSYSTEM
├── YOUTAG WELLNESS APP / PLATFORM
└── YOUTAG RECHARGES APP / PLATFORM
```

- `youtag_wellness_app/` — app/platform namespace for the YOUTAG Wellness experience.
- `youtag_recharges_app/` — app/platform namespace for the YOUTAG Recharges experience.

The two apps may have different user experiences, features, catalogs, service workflows and app integrations. Their common company/business identity remains the single YOUTAG business ecosystem.

## Architecture boundaries

This folder owns only the global business identity and app/platform directory. CORE owns canonical business rules and identities; API owns endpoint contracts; ENGINE owns workflows; DATABASE owns persistence; authentication, credentials, payments and provider connections remain in their respective layers.

Do not duplicate company identity, accounts, payment ledgers or shared business records for the two apps. Keep app-specific functionality separated where required while linking both apps to the same YOUTAG business identity.

## Verification boundary

This namespace does not establish that either app is connected to a live provider, that official APIs are available, or that account, payment or transaction operations are implemented. Those capabilities require verified provider documentation, credentials, contracts and tests.
