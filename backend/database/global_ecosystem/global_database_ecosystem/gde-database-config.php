<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/database.php';

/** Canonical GDE connection config alias; one central DB only. */
if (!function_exists('gde_database_config')) {
    function gde_database_config(): array
    {
        return supreme_main_database_connection_config();
    }
}
