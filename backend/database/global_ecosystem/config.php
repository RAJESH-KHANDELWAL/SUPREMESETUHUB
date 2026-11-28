<?php
declare(strict_types=1);
require_once dirname(__DIR__) . '/config.php';

/** GE identity gates all share one physical SUPREMESETUHUB database. */
if (!function_exists('global_ecosystem_config')) {
    function global_ecosystem_config(): array
    {
        $main = supreme_main_foundation_config();
        return [
            'id' => 'GLOBAL_ECOSYSTEM',
            'layer' => 'global_ecosystem',
            'parent' => 'SUPREMESETUHUB',
            'database_topology' => 'ONE_PHYSICAL_DATABASE_FOUR_LOGICAL_IDENTITY_GATES',
            'primary_identity' => $main['primary_identity'],
            'identities' => $main['identities'],
            'identity_gates' => $main['identity_gates'],
            'database' => $main['database'],
            'databases' => $main['databases'],
            'wordpress_database' => $main['wordpress_database'],
        ];
    }
}
