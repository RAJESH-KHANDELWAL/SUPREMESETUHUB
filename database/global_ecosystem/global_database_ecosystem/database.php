<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/database.php';

/** Generic GDE entry point; uses the one central PDO connection. */
if (!function_exists('global_database_ecosystem_database')) {
    function global_database_ecosystem_database(): PDO
    {
        return supreme_main_database_connection();
    }
}
