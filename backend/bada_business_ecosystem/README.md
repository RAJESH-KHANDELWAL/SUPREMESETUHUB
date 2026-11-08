# BADA BUSINESS ECOSYSTEM

Canonical root for the Bada Business product and provider-resource ecosystem.

## Canonical hierarchy
```
backend/
└── bada_business_ecosystem/
    ├── global_ecosystem/   # Global Bada Business platform/resource ecosystem
    └── api_ecosystem/      # API router exposure only
```

The global ecosystem owns provider profiles, platform links, referrals,
program records and other product-resource metadata.

The actual HTTP API implementation, schemas, routes, industry taxonomy and
integrations remain separately implemented under:
`backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`

The previous child package name `global_bada_business_ecosystem` is retired.
