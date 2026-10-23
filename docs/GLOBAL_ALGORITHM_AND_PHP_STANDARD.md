# SUPREMESETUHUB Advanced PHP Engineering Standard

## Scope

This document governs PHP code only. Global algorithms have a separate architecture, implementation directory, tests, and documentation; they must not be embedded in this PHP standard or implemented merely because PHP is available.

## PHP engineering baseline

- Use a maintained PHP 8.x release; this repository's PHP syntax CI targets PHP 8.3 and 8.5.
- Use `declare(strict_types=1)`, namespaces, typed parameters/returns and explicit exceptions in new PHP code.
- Keep provider credentials in deployment secret stores, not source files, frontend code, logs or test fixtures.
- Use prepared statements for SQL, allowlists for dynamic identifiers, output escaping appropriate to the destination, and server-side authorization for every private endpoint.
- Keep HTTP, database, filesystem and provider side effects behind explicit PHP-specific adapters.
- Preserve backward compatibility at WordPress and other PHP integration boundaries; add migration steps and tests before changing public interfaces.
- Do not automatically upgrade a live hosting account's PHP runtime from a repository change. Verify the host's available runtime, WordPress/theme/plugin compatibility and staging tests first.

## Quality gates

The `PHP Quality` GitHub Actions workflow lints tracked PHP files on PHP 8.3 and 8.5. Passing these checks demonstrates PHP syntax validity only; it does not prove WordPress compatibility, runtime behavior, provider connectivity or production readiness.

## Upgrade phases

1. Inventory every PHP entry point, WordPress plugin and PHP domain bridge; record runtime/version assumptions.
2. Upgrade PHP modules selectively, preserving their existing domain boundaries and public interfaces.
3. Add PHP-specific tests for validation, authorization, error handling and persistence.
4. Test WordPress plugin compatibility on staging before changing production behavior.
5. Verify deployed PHP versions and actual service configuration separately from CI.

## Official version policy

PHP's supported-versions page is the source of truth for active and security-support windows: https://www.php.net/supported-versions.php
