<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/config.php';

/**
 * Global Ecosystem exposes the complete five-database identity topology.
 * The four identity databases are separate databases governed by SUPREMESETUHUB.
 */
if (!function_exists('global_ecosystem_config')) {
    function global_ecosystem_config(): array
    {
        $main = supreme_main_foundation_config();
        return [
            'id' => 'GLOBAL_ECOSYSTEM',
            'layer' => 'global_ecosystem',
            'parent' => 'SUPREMESETUHUB',
            'primary_identity' => $main['primary_identity'],
            'identities' => $main['identities'],
            'identity_gates' => $main['identity_gates'],
            'database_topology' => 'ONE_MAIN_PLUS_FOUR_IDENTITY_DATABASES',
            'databases' => $main['databases'],
            'wordpress_database' => $main['wordpress_database'],
        ];
    }
}
