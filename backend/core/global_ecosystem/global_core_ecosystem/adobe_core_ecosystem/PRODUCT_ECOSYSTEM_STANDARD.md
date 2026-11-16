# Adobe Product Core Ecosystem Standard

Every canonical Core domain is represented by a product-family package scaffold. Each package contains ten responsibility directories: `authentication`, `capabilities`, `docs`, `events`, `lifecycle`, `models`, `schemas`, `security`, `services`, `tests`.

Each package also contains `README.md`, `__init__.py`, `ecosystem_config.py`, `ecosystem_manifest.json` and `service.py`.

## Layer boundaries

Core owns provider/product identity, capability metadata, lifecycle metadata, policy metadata, readiness and stable contracts. API owns OAuth, SDK clients, HTTP transport, endpoints and webhooks. Storage owns file/object persistence. Database owns durable structured records. Runtime/Engine owns jobs, queues, schedulers and execution. Application/UI owns user workflows and presentation.

## Completion criteria

A scaffold is complete only as a directory/template baseline. A production-ready product integration additionally requires verified product-specific capabilities, official API references, entitlement/scope checks, secure configuration, contract tests, error handling, observability and successful integration tests. No package may claim live connectivity without evidence.
