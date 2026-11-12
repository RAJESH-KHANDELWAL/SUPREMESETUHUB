<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/database.php';
require_once __DIR__ . '/gde-database-config.php';

/** Generic database entry point within Global Database Ecosystem. */
if (!function_exists('global_database_ecosystem_database')) {
    function global_database_ecosystem_database(): PDO
    {
        return gde_database_connection();
    }
}
