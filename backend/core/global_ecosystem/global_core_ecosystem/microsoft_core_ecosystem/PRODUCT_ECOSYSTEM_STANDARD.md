# Microsoft Product Ecosystem Standard

1. Keep one canonical provider registry and stable ecosystem IDs.
2. Keep product packages focused on one coherent provider capability; do not split every SKU, API operation or marketing label into a directory.
3. Product package names use `microsoft_<product>_core_ecosystem`.
4. Core owns metadata, classification, contracts and orchestration; API adapters own HTTP/SDK transport; auth owns OAuth and credentials; persistence owns database access.
5. A registered capability is not an authorization grant, entitlement or live integration.
6. Use tenant-scoped context for operations and least-privilege scopes in API/auth layers.
7. Never store access tokens, refresh tokens, client secrets, API keys or passwords in catalog files.
8. Add Python/PHP files only when they contain a tested, owned responsibility. Do not add placeholder files to every product directory.
9. Extend domain mapping and tests whenever a product family is added.
10. Preserve existing product directories and central database configuration.
