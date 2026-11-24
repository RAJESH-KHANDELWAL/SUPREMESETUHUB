<?php
declare(strict_types=1);
require_once dirname(__DIR__) . '/database.php';
/** Resolve a named identity database; default to SUPREMESETUHUB for compatibility. */
if (!function_exists('global_ecosystem_database')) {
    function global_ecosystem_database(string $identity = 'SUPREMESETUHUB'): PDO
    {
        return supreme_identity_database_connection($identity);
    }
}
