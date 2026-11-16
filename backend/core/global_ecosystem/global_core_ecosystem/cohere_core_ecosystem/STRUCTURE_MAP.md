# Cohere CORE Structure Map

**Repository path:** `backend/core/global_ecosystem/global_core_ecosystem/cohere_core_ecosystem/`

This map explains the current directory layout. It records the existing structure; it does not imply that every integration is implemented.

```text
cohere_core_ecosystem/
├── README.md                    # Entry point and operating boundary
├── ARCHITECTURE.md              # Component and layer ownership
├── IMPLEMENTATION_STATUS.md     # Implemented vs pending work
├── STRUCTURE_MAP.md             # This directory guide
├── __init__.py                  # Public package exports
├── ecosystem_config.py          # Non-secret defaults
├── ecosystem_manifest.json      # Machine-readable status and capability list
├── contracts.py                 # Shared request/result dataclasses
├── manager.py                   # Public manager facade
├── service.py                   # Shared capability validation service
├── policies.py                  # CORE operation restrictions
├── capabilities/
│   └── catalog.py               # Five canonical capability identifiers
├── cohere_classify_core_ecosystem/
│   ├── README.md
│   ├── __init__.py
│   ├── contracts.py
│   ├── php/
│   └── .gitkeep                 # Git placeholder only, where present
├── cohere_command_core_ecosystem/
│   └── [same package pattern]
├── cohere_embed_core_ecosystem/
│   └── [same package pattern]
├── cohere_rerank_core_ecosystem/
│   └── [same package pattern]
├── cohere_tokenize_core_ecosystem/
│   └── [same package pattern]
├── authentication/              # Secure-runtime boundary documentation
├── models/                      # Capability descriptor
├── schemas/                     # Request payload shape helper
├── security/                    # Secret-field policy
├── lifecycle/                   # Ecosystem state enum
├── events/                      # Event payload contract
├── services/                    # Capability registry lookup helper
├── php/                         # Shared PHP interoperability contract
└── tests/                       # Shared CORE unit tests
```

## Five capability packages

| Package | Request type | Input validation intent |
|---|---|---|
| `cohere_classify_core_ecosystem` | `ClassifyRequest` | Non-empty text inputs |
| `cohere_command_core_ecosystem` | `CommandRequest` | Non-empty message |
| `cohere_embed_core_ecosystem` | `EmbedRequest` | Non-empty text inputs |
| `cohere_rerank_core_ecosystem` | `RerankRequest` | Query, documents and positive optional top-N |
| `cohere_tokenize_core_ecosystem` | `TokenizeRequest` | Non-empty text |

## Important distinction

Cohere CORE is organized around **five capabilities**. It is not a 129-offering product catalog like the Google CORE inventory. Do not create artificial product families or duplicate Google-specific subfolder patterns here. Add a new Cohere capability only when its contract, ownership and provider/API/ENGINE boundary are defined.

## Current status

The capability packages and shared components define contracts and validation foundations. Live provider transport, credentials, execution and persistence belong to other layers and are not enabled by this directory.
