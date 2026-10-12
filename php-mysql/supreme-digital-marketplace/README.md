# SUPREME DIGITAL DESIGN MARKETPLACE (PHP + MySQL)

This is the PHP/MySQL foundation for the **digital-only** SUPREME design store. It is separate from physical print fulfillment: no inventory, printing, packing, or shipping tables are included.

## Folder map

- `config/.env.example` — names of environment variables; never put real passwords here.
- `database/schema.sql` — MySQL tables for original digital designs, market-specific prices, trend signals, digital orders, order items, and secure download entitlements.
- `src/Database.php` — PDO MySQL connection using environment variables.
- `src/DigitalDesignRepository.php` — prepared-statement catalog query.
- `public/api/designs.php` — read-only JSON catalog for published designs.
- `tests/README.md` — local smoke-test checklist.

## Install

1. Use PHP 8.2+ with PDO MySQL enabled and MySQL 8.0+.
2. Create a dedicated database and least-privilege database user.
3. Import `database/schema.sql` into that database.
4. Set `SUPREME_DB_HOST`, `SUPREME_DB_PORT`, `SUPREME_DB_NAME`, `SUPREME_DB_USER`, and `SUPREME_DB_PASSWORD` as server environment variables.
5. Configure the web server document root to this module's `public/` directory. Keep `src/`, `config/`, and `database/` outside the public document root.
6. Open `/api/designs.php?market=IN` or `/api/designs.php?market=GLOBAL`.

## Pricing convention

`price_minor` stores integer minor currency units to avoid floating-point money errors: INR is stored in paise (₹500.00 = 50000), USD in cents ($5.00 = 500). The catalog response formats this as a decimal amount.

## Security and production status

- The catalog returns only published designs and their public preview paths. It never returns private original-file storage keys.
- Database access uses PDO prepared statements and credentials come only from environment variables.
- Keep original downloadable files in private object storage; do not place them under `public/`.
- A paid order must only create a download entitlement after the payment provider's signed webhook is verified server-side. Store a hash of a random download token, not the raw token.
- Configure real user authentication, payment provider verification, rate limiting, secure download delivery, and privacy/consumer-law handling before accepting real payments.
- Trend signal rows are a data model only; no live trend provider is connected yet. AI image generation, payment checkout, and secure download delivery are not claimed as implemented here.

## Relationship to the current application

The existing SUPREMESETUHUB application runs on Python/FastAPI with SQLite. This folder is an explicit PHP/MySQL module, not automatically executed by that FastAPI process. It needs a PHP-capable runtime and MySQL database, then a deliberate integration/deployment step. Do not store real credentials in GitHub.
