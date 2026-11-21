# GLOBAL BADA BUSINESS — CULTURE SERVICE / WORK / BUSINESS CORE

Integrated child package under Global Bada Business CORE. It classifies capabilities in SERVICE, WORK and BUSINESS and provides record validation/publication governance.

**Boundaries:** Culture knowledge/domain source remains the dedicated Culture CORE. This package does not duplicate knowledge, claim live provider listings/jobs, perform transactions, or store provider URLs/prices. It is classification/governance only.

**Coverage (12 capability records):** education; translation/localization; heritage conservation; arts/crafts/design; cultural tourism; festivals/events; research/publishing; media/content production; traditional knowledge education; community organizations; performing arts; cultural advisory.

**Use:** import `GlobalBadaBusinessCultureServiceWorkBusinessManager` from this package, call `status()`, `catalogue(domain)`, `capability(id)`, `validate(record)`, and `can_publish(record)`. Publication requires valid record and APPROVED status.
