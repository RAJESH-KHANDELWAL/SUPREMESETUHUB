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

## Owner-provided referral profile

The owner-provided YOUTAG referral profile is stored in `referral_profiles/rajesh_khandelwal.json`. It records Referral ID `2043272`, owner `Rajesh Khandelwal`, and the exact Google Play URL supplied by the owner. The owner states that this is the personal referral link for YOUTAG WELLNESS and YOUTAG RECHARGES. The package identifier in the supplied URL is `com.youtagindia.business`; separate attribution for each app is not independently verified. Treat the profile as public referral metadata, not an authentication credential or proof of a completed registration.

## Architecture boundaries

This folder owns only the global business identity and app/platform directory. CORE owns canonical business rules and identities; API owns endpoint contracts; ENGINE owns workflows; DATABASE owns persistence; authentication, credentials, payments and provider connections remain in their respective layers.

Do not duplicate company identity, accounts, payment ledgers or shared business records for the two apps. Keep app-specific functionality separated where required while linking both apps to the same YOUTAG business identity.

## Verification boundary

This namespace does not establish that either app is connected to a live provider, that official APIs are available, or that account, payment or transaction operations are implemented. Those capabilities require verified provider documentation, credentials, contracts and tests.

## Owner-provided YOUTAG referral link

- Owner: Rajesh Khandelwal
- Referral ID: `2043272`
- Registration link: [Install YOUTAG Business and register with referral ID 2043272](https://play.google.com/store/apps/details?id=com.youtagindia.business&referrer=utm_source%3Dgoogle%26utm_campaign%3D2043272)
- App package: `com.youtagindia.business`
- Owner-declared scope: YOUTAG WELLNESS and YOUTAG RECHARGES; the supplied Play Store URL identifies the Business app package, and separate app attribution has not been independently verified.
- Canonical source of truth: `backend/global_ecosystem/global_bada_business_ecosystem/global_network_marketing_direct_selling_business_ecosystem/global_youtag_business_ecosystem/referral_profiles/rajesh_khandelwal.json`

Keep the URL exactly as supplied. This is owner-provided public referral metadata, not an API credential or proof of registration, commission, provider partnership or live integration. Read the canonical profile rather than creating alternate referral records.

## Company knowledge base — 2026

Searchable Hinglish source reference: [`company_knowledge/YOUTAG_WELLNESS_BASIC_KNOWLEDGE_2026_HINGLISH.md`](company_knowledge/YOUTAG_WELLNESS_BASIC_KNOWLEDGE_2026_HINGLISH.md). It covers the company profile, terms, principles, ranks, 20-level plan, source-stated income categories and rank benefits, plus verification gaps. It is transcribed from the owner-uploaded five-page 2026 PDF. The figures and business/earnings claims are source statements, not independently verified facts or guaranteed outcomes. Consult current official documents before relying on them.
