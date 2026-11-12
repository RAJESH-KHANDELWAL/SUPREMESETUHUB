<?php
declare(strict_types=1);

require_once __DIR__ . '/global_database_ecosystem/gde-database-config.php';

/** GE connection config resolves through the nested GDE database owner. */
if (!function_exists('ge_database_config')) {
    function ge_database_config(): array
    {
        return gde_database_config();
    }
}
