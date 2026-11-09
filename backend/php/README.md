# PHP Runtime Layer

This directory contains the framework-neutral PHP runtime primitives used by
PHP integrations and optional WordPress-facing adapters.

## Bootstrap

Load the PHP layer with:

```php
require_once __DIR__ . '/bootstrap.php';
```

The bootstrap loads `GlobalAlgorithmKernel.php` exactly once. It does not
start the Python/FastAPI backend, connect to external services, or load
credentials.

## Global Algorithm Kernel

Namespace: `SupremeSetuHub\\GlobalCore`

The kernel currently provides:

- `normalizeIdentifier()`: normalize labels into stable URL-safe identifiers.
- `canonicalJson()`: recursively sort associative keys and encode JSON.
- `stableHash()`: hash canonical JSON for deterministic fingerprints.
- `paginate()`: bounded array pagination with metadata.
- `retryDelaySeconds()`: capped exponential retry delay.
- `redact()`: recursively redact common credential and secret fields.

These are deterministic utility primitives, not a replacement for the Python
CORE, ENGINE, DATABASE, STORAGE, API, authentication, or authorization layers.

## Requirements

- PHP 8.1 or newer (uses union/mixed types, `array_is_list()`, and
  `str_ends_with()`).
- No third-party PHP packages are required.

## Smoke test

From the repository root:

```sh
php backend/tests/php/global_algorithm_kernel_test.php
php -l backend/php/bootstrap.php
php -l backend/php/GlobalAlgorithmKernel.php
```
