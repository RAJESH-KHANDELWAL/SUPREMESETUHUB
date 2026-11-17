# GLOBAL HUMAN LANGUAGE CORE ECOSYSTEM

A first-class, independently registered **CORE ecosystem**, structured on the same package pattern as `google_core_ecosystem/`.

## Canonical package layout

- `README.md` — ecosystem scope, standards and governance
- `__init__.py` — public Python interface
- `catalog.py` and `catalog.json` — read-only domain/provider catalog
- `constants.py` — canonical ecosystem identity and layer metadata
- `contracts.py` — typed domain and service-tier contracts
- `ecosystem_manifest.json` — machine-readable identity and policy manifest
- `orchestrator.py` — read-only discovery and orchestration
- `policy.py` — privacy, age-assurance, consent and moderation metadata
- `service.py` — read-only service facade
- domain directories — human-language taxonomy and provider domains

## Coverage

- **Bharat / Indic:** scheduled, regional, classical, tribal, indigenous and community languages
- **Global:** natural spoken, written and signed languages, families, macrolanguages and variants
- **Writing systems:** scripts, orthographies, Unicode, directionality, romanization and transliteration
- **Language services:** dictionaries, lexicons, detection, OCR, speech, translation, interpretation, localization and learning
- **Preservation:** endangered and indigenous language documentation and revitalization
- **Provider metadata:** Alibaba, AWS, Baidu, DeepL, Google, IBM, Microsoft, Naver, OpenAI, Tencent and Yandex

## Separation boundary

Programming-language taxonomy and developer tooling belong only in the sibling `global_programming_language_core_ecosystem/`. This ecosystem contains human-language domains only. Shared infrastructure is implemented within this package; there is no duplicate `global_language_core_ecosystem/` package.

## Standards and completeness

Use stable identifiers such as ISO 639, BCP 47 and ISO 15924 where applicable. The catalog is extensible and is **not** a claim that every language, dialect or sign language has already been exhaustively enumerated. Respect community names and preferred endonyms.

## Adult-content boundary

Only lawful content involving consenting adults is in scope. Exclude minors and any sexualization of minors, non-consensual intimate imagery, coercion, trafficking, exploitation and illegal content. Adult classification is not itself consent or proof of legality. Apply jurisdictional age checks, consent/rights verification, moderation and takedown procedures before any runtime service.

## Tier model

Normal → Basic → Standard → Premium → Professional → Enterprise → Supreme. Tiers describe service capabilities and quality targets, not permission to bypass law, consent or safety.
