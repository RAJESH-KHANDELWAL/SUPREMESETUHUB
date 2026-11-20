# Architecture

GLOBAL DOMAIN CORE is a metadata/governance layer only.

| Layer | Ownership |
|---|---|
| Core | Registry, taxonomy, policy, lifecycle metadata, readiness |
| API | Provider HTTP/SDK calls, auth, normalization |
| Storage/Database | Durable tenant data, schemas and migrations |
| Engine | Jobs, retries, schedules and execution |
| Application | User workflows, consent and UI |

Security: tenant context is authenticated upstream; secrets use external secret storage; write actions require explicit authorization; live status requires deployed smoke tests. Catalog presence does not establish adapter implementation.
