# GLOBAL ENTITY RELATIONSHIPS CORE ECOSYSTEM

The parent CORE defines a canonical 36-category taxonomy and 21 relationship types. Each of its 36 category subfolders is populated with Python manager, PHP facade, package export, and README. Category-specific required-field contracts are maintained in the shared submodule manager and keyed by folder.

## Child folder work
- 36 category submodules (including the taxonomy and relationship-tier categories)
- 1 data helper folder for read-only reference metadata
- 1 tests folder with contract coverage for every category manager
- Each category manager validates input metadata and evidence, and explicitly reports no live connection or persistence.

## Naming convention
Ecosystem display names: GLOBAL + SUBJECT + CORE ECOSYSTEM. IDs: GLOBAL-SUBJECT-CORE-ECOSYSTEM. Every category manager derives the display name and ID from its folder name.

## Boundaries and limitations
Catalog and validation only; not a relationship database, not live APIs, and not a source of verified ownership/affiliation/consent/licensing. Verified status requires HTTP(S) evidence. Data minimization, consent and lawful adult-only safeguards apply to sensitive relationship categories.

## Master catalog
Read-only reference to backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json; 2468 target remains separate and is not copied or modified by this module.
