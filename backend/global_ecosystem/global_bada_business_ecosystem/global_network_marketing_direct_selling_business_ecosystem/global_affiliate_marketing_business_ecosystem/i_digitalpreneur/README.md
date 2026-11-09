# iDigitalPreneur PLATFORM

Parent category: `GLOBAL-AFFILIATE-MARKETING-BUSINESS-ECOSYSTEM`

Platform namespace for iDigitalPreneur within the global affiliate-marketing directory.

## Source documents indexed

The owner-provided brochures have been read and organized into source-based Markdown knowledge files:

- [The Brief — Package & Course Catalogue](catalogs/THE_BRIEF_PACKAGE_AND_COURSE_CATALOG.md) — package prices, brochure-stated course counts and referral commissions, package stacking, course titles/languages, and source page references.
- [Premium Plus Package Guide](catalogs/PREMIUM_PLUS_PACKAGE_GUIDE.md) — Premium Plus price and affiliate benefit as printed, numbered courses, modules, FAQ statements and brochure value estimates.
- [Training & Instructor Directory](catalogs/TRAINING_AND_INSTRUCTORS.md) — training program descriptions and instructor names as printed in the brochure.

## Source-file register

| Source filename | Pages | Handling |
|---|---:|---|
| `The_Brief_New_Brochure_compressed (1).pdf` | 62 | Read and indexed in Markdown |
| `Premium_Plus_Package_Brochure_compressed (1).pdf` | 27 | Read and indexed in Markdown |
| `Premium_Plus_Package_Brochure_compressed (2).pdf` | 27 | Identical duplicate of the first Premium Plus PDF; indexed once |

The Markdown files are searchable knowledge-base extracts. The original PDF binaries are not stored in this repository in this update.

## Data provenance and verification

All package prices, promocode prices, course counts, commission amounts, access statements, value estimates, instructor biographies and training descriptions are transcribed from the supplied brochures. They are not independently verified current commercial terms. Confirm current package entitlements, affiliate eligibility, payout rules, course availability and legal terms with iDigitalPreneur before purchase, promotion or financial decisions.

## Architecture boundaries

Keep this directory as the platform's global identity, source-document index and catalog namespace. Do not put credentials, affiliate account records, payout ledgers or live provider integrations here.

- CORE owns canonical platform identity and business rules.
- API owns endpoint contracts and provider-facing interfaces.
- ENGINE owns orchestration and workflows.
- DATABASE owns persistence and schema.
- STORAGE owns file/object storage and retention.
- AI may consume these source documents through its own retrieval/indexing interface; it must not become the owner of the canonical source files.

No official API, affiliate approval, payout processing, course entitlement, or live connection is implied by this namespace.
