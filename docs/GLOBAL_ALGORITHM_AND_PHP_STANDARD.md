# SUPREMESETUHUB Global Algorithm and Advanced PHP Standard

## Purpose

Provide a shared, testable PHP utility layer for PHP-enabled modules without replacing the primary FastAPI/Python backend or collapsing domain-specific modules into one implementation.

## Shared algorithm kernel

`backend/php/GlobalAlgorithmKernel.php` currently provides:

- **Identifier normalization** for stable, bounded machine identifiers.
- **Canonical JSON and stable hashing** so associative key order does not change the hash. List order is preserved.
- **Bounded pagination** with explicit metadata and a configurable maximum page size.
- **Capped exponential retry delays** to avoid unbounded backoff.
- **Recursive secret redaction** for common credential-like key names before diagnostic serialization.

These are primitives, not a complete authorization, cryptography, fraud detection, recommendation, or business rules engine. Each domain must define its own policies and test its own behavior. Do not use a plain hash as a password hash or as a substitute for an HMAC/signature protocol.

## PHP engineering baseline

- Use a maintained PHP 8.x release; this repository's shared kernel and CI target PHP 8.3 and 8.5.
- Use `declare(strict_types=1)`, namespaces, typed parameters/returns and explicit exceptions in new core code.
- Keep provider credentials in deployment secret stores, not source files, frontend code, logs or test fixtures.
- Use prepared statements for SQL, allowlists for dynamic identifiers, output escaping appropriate to the destination, and server-side authorization for every private endpoint.
- Keep HTTP, database, filesystem and provider side effects behind explicit adapters; algorithms should be deterministic and independently testable where possible.
- Preserve each module's ownership of domain tables and business rules. Shared utilities do not mean all modules should share one table or one runtime.
- Maintain backward compatibility at integration boundaries; add migration steps and tests before changing public interfaces.
- Do not automatically upgrade a live hosting account's PHP runtime from a repository change. Verify the host's available runtime, WordPress/theme/plugin compatibility and staging tests first.

## Quality gates

The `PHP Quality` GitHub Actions workflow lints tracked PHP files and runs the standalone global-kernel tests on PHP 8.3 and 8.5. Passing these checks demonstrates syntax and the included unit behaviors only; it does not prove all WordPress installations, hosting environments, APIs or production integrations work.

## Next integration phases

1. Inventory every PHP entry point, WordPress plugin and domain bridge; record runtime/version assumptions.
2. Add adapters selectively where PHP modules genuinely need shared primitives.
3. Add module-level tests for input validation, authorization, error handling, persistence and cross-user isolation.
4. Test WordPress plugin compatibility on staging before changing production plugin behavior.
5. Verify deployed PHP versions and actual service configuration separately from CI.

## Official version policy

PHP's supported-versions page is the source of truth for active and security-support windows: https://www.php.net/supported-versions.php
