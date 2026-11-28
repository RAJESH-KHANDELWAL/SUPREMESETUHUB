# Platform Registry Data

`platform_registry.json` is the canonical read-only profile source. It starts empty. Add only stable platform IDs, official source URLs, country availability, domain/type, operator/owner relationship references and explicit verification state. Never mark a record verified without traceable sources. Adult records must set `adult_only: true` and `minimum_age: 18`; general searches exclude them by default.
