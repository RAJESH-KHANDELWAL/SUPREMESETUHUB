<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/database.php';

/** Legacy GE config name; routes to the single central database. */
if (!function_exists('ge_database_config')) {
    function ge_database_config(): array
    {
        return supreme_main_database_connection_config();
    }
}
