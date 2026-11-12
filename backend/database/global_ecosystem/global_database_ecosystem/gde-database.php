<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/database.php';

/**
 * Backwards-compatible GDE connection function.
 * It resolves to SUPREMESETUHUB's one central database connection.
 */
if (!function_exists('gde_database_connection')) {
    function gde_database_connection(): PDO
    {
        return supreme_main_database_connection();
    }
}
