<?php
declare(strict_types=1);

require_once __DIR__ . '/ge-database.php';

/** Stable generic entry point for the Global Ecosystem database layer. */
if (!function_exists('global_ecosystem_database')) {
    function global_ecosystem_database(): PDO
    {
        return ge_database_connection();
    }
}
