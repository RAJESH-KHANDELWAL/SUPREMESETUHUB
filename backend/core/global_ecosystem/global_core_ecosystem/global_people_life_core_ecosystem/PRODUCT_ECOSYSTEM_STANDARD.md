# PEOPLE LIFE CORE — PRODUCT ECOSYSTEM STANDARD

1. One canonical domain per capability; shared capabilities are referenced, not copied.
2. Local domain packages are metadata managers over the shared `domain_runtime.py`; do not duplicate business logic in each domain.
3. Existing module directories remain compatibility/capability modules. Their domain relationships are declared in `catalog.json` and `domain_catalog.py`.
4. Adult-specific implementation is canonical in the Kamasutra ecosystem. People Life exposes five 18+ domain references and does not duplicate adult provider/content implementations.
5. Service tiers are configuration metadata: Normal, Basic, Standard, Premium, Professional, Enterprise and Supreme.
6. Age-sensitive or regulated workflows require independent application authorization, reliable age assurance where required, informed consent, jurisdictional review and qualified providers.
7. Core must not store credentials, sensitive personal records, intimate media or health records, and must not execute payments, clinical care, legal representation or crisis response.
8. Add a folder only when it owns a distinct domain responsibility and has a real manager/runtime need. Do not create empty generic folders or duplicate shared files.
9. Every module must map to at least one domain or a service tier. New categories should update the canonical catalog and tests together.
10. Taxonomy and registry entries are architecture metadata and do not increase the 2,468 unique-topic master catalogue count.
