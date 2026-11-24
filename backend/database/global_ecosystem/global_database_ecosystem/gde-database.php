<?php
declare(strict_types=1);
require_once dirname(__DIR__, 2) . '/database.php';
/** GDE connection entry point; select MAIN or one of the four identity DBs. */
if (!function_exists('gde_database_connection')) {
    function gde_database_connection(string $identity = 'SUPREMESETUHUB'): PDO
    {
        return supreme_identity_database_connection($identity);
    }
}
