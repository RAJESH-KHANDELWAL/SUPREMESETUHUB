# OpenAI Product Core Ecosystem Standard

OpenAI Core follows the Google Core responsibility pattern while using OpenAI's actual product taxonomy.

Each product package contains only:
- `__init__.py`: stable package export.
- `service.py`: a thin product-specific binding to the shared Core product service.
- `README.md`: product scope, status and layer boundaries.

Shared contracts, policy, catalog, lifecycle metadata, domain runtime and orchestration stay at the provider root. Do not copy a complete manager into every product package or create empty placeholder directories.

Product/service identities are sourced from the OpenAI product registry. API capability families (Responses, models, embeddings, images, audio, files, batch, vector stores, moderation, evaluations and webhooks) remain separate from named product families.

Core is metadata-only. API transport, SDK calls, credential validation, secret persistence, billing, model inference and ENGINE execution belong to their respective layers.
