# GLOBAL ENTITY RELATIONSHIPS CORE ECOSYSTEM

Canonical taxonomy, relationship types, validation policy and discovery metadata for connecting entities without duplicating entity identities.

## Naming standard
Every CORE ecosystem record follows **GLOBAL + SUBJECT + CORE ECOSYSTEM** and ID **GLOBAL-SUBJECT-CORE-ECOSYSTEM**. Provider/category names are normalized consistently; documentation/data/test folders are not ecosystem records.

## Coverage
This CORE includes 36 taxonomy categories: adult industry relationship categories; age verification and consent; brand/trademark; partner/supplier; commerce marketplace; ownership/control and corporate groups; dating platform; developer/API provider; digital platform/social media; founder/director/management; global and India entities; relationship tiers; payments/finance; provenance/verification; sexual health and wellness education; trust/safety/moderation.

## Data model
Relationship edges require stable relationship ID, source entity ID, target entity ID, relationship type, verification status, optional jurisdiction and effective dates, evidence source URLs and metadata. Verified claims must include HTTP(S) evidence. Self-edges are rejected. Unverified and pending records are not treated as factual claims.

## Layer boundaries
CORE owns taxonomy, metadata, policy and read-only discovery. API owns routes/contracts, ENGINE owns execution orchestration, DATABASE owns persistence, STORAGE owns artifacts, and external provider adapters belong in the appropriate integration/API layer. Credentials are not stored here. No live provider connections are claimed.

## Master 2468 catalog
Reference-only, on-demand pointer to `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` (target 2468; current numbered inventory remains separate). CORE does not duplicate, edit, or count its numbered entries.

## Safety and privacy
Minimize personal data and use public or consented professional data. Do not infer ownership, affiliation, consent, licensing, age or API access from a directory entry. Adult-related categories are limited to lawful, consenting adults (18+); prohibit minors, exploitation, non-consensual sexual content and illegal content; age-verification, consent, privacy and reporting controls are required where applicable.

## Status
Catalog/taxonomy implementation only. Tests are authored; execution/CI must confirm before calling runtime validation complete. This module is not a live relationship database and does not assert any real-world relationship.
