<?php
declare(strict_types=1);

/** Global Ecosystem parent-layer identity and routing configuration. */
if (!function_exists('global_ecosystem_config')) {
    function global_ecosystem_config(): array
    {
        return [
            'id' => 'GLOBAL_ECOSYSTEM',
            'layer' => 'global_ecosystem',
            'parent' => 'MAIN_BASE_FOUNDATION',
            'database_child' => 'global_database_ecosystem',
            'connection_owner' => 'global_database_ecosystem',
        ];
    }
}
