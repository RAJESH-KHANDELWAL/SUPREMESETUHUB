<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/database.php';
require_once __DIR__ . '/gde-database-config.php';

/**
 * Physical GDE connection. This only opens a PDO connection.
 * It does not create, migrate, truncate, or write tables.
 */
if (!function_exists('gde_database_connection')) {
    function gde_database_connection(): PDO
    {
        static $connection = null;
        if ($connection instanceof PDO) {
            return $connection;
        }
        $connection = supreme_database_connect(gde_database_config());
        return $connection;
    }
}
