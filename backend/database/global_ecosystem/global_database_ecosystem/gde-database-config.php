<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/config.php';

/** Canonical GDE Hostinger MariaDB/MySQL connection configuration. */
if (!function_exists('gde_database_config')) {
    function gde_database_config(): array
    {
        return supreme_database_config('GDE_DB_');
    }
}
