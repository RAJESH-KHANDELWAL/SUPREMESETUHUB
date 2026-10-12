# PHP/MySQL module smoke checks

Run these checks in a PHP 8.2+ environment with the PDO MySQL extension enabled.

1. Syntax-check the PHP source files:
   ```sh
   php -l src/Database.php
   php -l src/DigitalDesignRepository.php
   php -l public/api/designs.php
   ```
2. Create a disposable MySQL 8 database and import `database/schema.sql`.
3. Verify all six tables exist: `digital_designs`, `digital_design_prices`, `design_trend_signals`, `digital_orders`, `digital_order_items`, and `digital_download_grants`.
4. Insert one design with status `PUBLISHED` and active INR/INR pricing; request `/api/designs.php?market=IN` and confirm the catalog returns it.
5. Confirm a `DRAFT` design is not returned and invalid markets/methods are rejected.
6. Confirm the JSON response does not contain `private_storage_key`, raw download tokens, or database credentials.

These are manual smoke-test instructions, not a claim that a live MySQL instance or production payment flow has been tested.
