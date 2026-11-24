<?php
declare(strict_types=1);
require_once dirname(__DIR__) . '/database.php';
/** Return the five named connection configurations. */
if (!function_exists('ge_database_config')) {
    function ge_database_config(): array
    {
        return supreme_main_foundation_config()['databases'];
    }
}
