# Global Database Ecosystem

Provider-neutral database ecosystem catalog covering Bharat, regional markets, and global deployments—from Normal through Supreme maturity.

## Scope
- Database models: relational SQL, distributed SQL, document, key-value, wide-column, graph, time-series, search/analytics, vector/AI, object/lakehouse, embedded/edge, ledger/event, cache/session, warehouse/OLAP, backup/recovery.
- Workload domains: public services, finance, commerce, industry, education/media, health/research, communications, security/identity, AI/automation, and lawful adult-oriented services involving consenting adults only.
- Geographic coverage taxonomy: India (states, union territories, districts, cities, rural/urban), South Asia, Asia Pacific, Middle East, Europe, Africa, North America, Latin America, and cross-border global environments.
- Maturity taxonomy: Normal, Standard, Professional, Enterprise, Advanced, Supreme.

## Adult-oriented data workloads
The catalog classifies adult creator accounts, age-assurance status, consent/release evidence, content metadata, subscription entitlements, payout ledgers, moderation, copyright/takedown, and privacy requests. This is database workload metadata, not a content library or a content distribution system.

Mandatory controls include lawful adult-only operation, robust age assurance, recorded and revocable consent where required, data minimization, encryption, access restrictions, retention/deletion controls, and appropriate moderation/takedown workflows. The ecosystem explicitly excludes exploitation, trafficking, coercion, minors, and non-consensual intimate imagery.

## Code layout
- `catalog.py`: geographic, maturity, database-model, workload, and guardrail taxonomy.
- `models.py`: typed metadata records for platforms, capabilities, and workloads.
- `registry.py`: thread-safe in-memory metadata registry; it does not persist data.
- `classification/`: workload classification helpers and adult-data safeguards.
- `platforms/`: provider-neutral database platform metadata catalog.
- `tests/`: offline taxonomy, classification, and registry tests.

## Architecture boundary
This package owns taxonomy, workload classification, catalog metadata, and discovery descriptors. Canonical DATABASE owns database drivers, secrets, connection pools, query execution, transactions, migrations, replication runtime, backup execution, and persistence. API, CORE, ENGINE, SECURITY, IDENTITY, and authorization remain separately owned layers. Provider-specific folders should expose adapter metadata and must not duplicate shared database runtime.

## Integration status
**Taxonomy only.** No provider credentials, live database connections, production persistence, or external integration has been configured or verified by these files.

## Validation
Run the repository's test runner with this package importable, for example:
`pytest backend/global_ecosystem/global_database_ecosystem/tests`
