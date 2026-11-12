<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/database.php';

/** Stable Global Ecosystem entry point; uses the central connection. */
if (!function_exists('global_ecosystem_database')) {
    function global_ecosystem_database(): PDO
    {
        return supreme_main_database_connection();
    }
}
