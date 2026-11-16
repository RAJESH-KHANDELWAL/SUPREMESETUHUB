<?php
declare(strict_types=1);
require_once dirname(__DIR__) . '/database.php';
/** Legacy GE connection entry point with explicit identity selection. */
if (!function_exists('ge_database_connection')) {
    function ge_database_connection(string $identity = 'SUPREMESETUHUB'): PDO
    {
        return supreme_identity_database_connection($identity);
    }
}
