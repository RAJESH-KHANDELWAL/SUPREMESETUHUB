# GLOBAL SOFTWARE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_software_core_ecosystem/`

## Mission

Provider-neutral control plane for software identity, provider/product catalogs, software domains, lifecycle and support metadata, license-reference boundaries, capability classification, policy and readiness.

## Architecture

- `catalog.py`: canonical provider registry and ecosystem identity.
- `contracts.py`: tenant context, software reference, readiness and result contracts.
- `domain_catalog.py` / `domain_runtime.py`: canonical domain taxonomy and shared read-only domain manager.
- `module_service.py`: provider-specific read-only Core service.
- `policy.py`: metadata sanitization and capability risk classification.
- `orchestrator.py`: provider/domain discovery and health metadata.
- `service.py`: public ecosystem status.
- `manager.py`: stable Python entry point.
- `manager.php`: thin PHP interoperability facade; no duplicated business logic.
- `global_*_core_ecosystem/`: shared domain packages.
- Existing provider packages: Adobe, Apple, AWS, GitHub, Atlassian and Microsoft.

## Domain coverage

1. **Software Governance** — Software identity, lifecycle, classification, licensing metadata and provider governance.\n2. **Operating Systems** — Desktop, server, mobile, embedded and real-time operating systems.\n3. **Desktop and Productivity** — Office suites, notes, calendars, collaboration clients and personal productivity.\n4. **Business and Enterprise** — ERP, CRM, HRM, finance, operations, enterprise resource planning and business suites.\n5. **Development and IDE** — IDEs, code editors, SDKs, compilers, build systems, debugging and developer workbenches.\n6. **DevOps and Delivery** — Source control, CI/CD, release engineering, artifact management and deployment workflows.\n7. **Cloud and Infrastructure** — Cloud platforms, infrastructure management, virtualization, containers and orchestration.\n8. **Database and Data** — Relational, document, graph, key-value, time-series databases, data platforms and ETL.\n9. **AI and Machine Learning** — Model development, inference platforms, ML operations, generative AI and data science software.\n10. **Security and Privacy** — Endpoint security, identity, access, encryption, vulnerability management and privacy tools.\n11. **Design and Creative** — Graphic design, UI/UX, 3D, CAD, video, audio, animation and creative production software.\n12. **Web and Content** — CMS, website builders, e-commerce platforms, publishing, web frameworks and content systems.\n13. **Communication and Collaboration** — Email clients, messaging, meetings, team collaboration and unified communications software.\n14. **Analytics and Observability** — BI, reporting, telemetry, logging, monitoring, tracing and performance analysis.\n15. **Networking and Systems** — Network management, DNS, remote access, system administration and infrastructure utilities.\n16. **Mobile and Applications** — Mobile applications, app frameworks, app distribution, testing and device software.\n17. **Gaming and Interactive** — Game engines, game development, launchers, simulation and interactive entertainment software.\n18. **Licensing Support and Interoperability** — Software licensing, subscriptions, support lifecycle, compatibility, migration and interoperability.

## Layer boundaries

Core owns catalog and policy metadata only. Provider API calls, OAuth, SDKs and transport belong in the API layer; secrets belong in an external secret manager; persistence belongs in Storage/Database; execution belongs in Runtime/Engine; billing transactions belong in Finance/Payments; UI belongs in Application.

## Safety and accuracy

A catalog entry does not prove that software is installed, licensed, supported on a particular device, deployed, or connected. Never store passwords, license keys, API keys, access tokens or private keys in this package. Mark live connectivity only after deployment authentication and provider smoke tests. Product inventories must be sourced and reviewed; do not invent product names or API availability.
