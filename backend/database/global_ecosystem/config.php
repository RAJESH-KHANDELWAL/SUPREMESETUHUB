<?php
declare(strict_types=1);

require_once dirname(__DIR__) . '/config.php';

/** Global Ecosystem is an identity gate under the SUPREMESETUHUB main identity. */
if (!function_exists('global_ecosystem_config')) {
    function global_ecosystem_config(): array
    {
        $main = supreme_main_foundation_config();
        return [
            'id' => 'GLOBAL_ECOSYSTEM',
            'layer' => 'global_ecosystem',
            'parent' => $main['primary_identity'],
            'primary_identity' => $main['primary_identity'],
            'identities' => $main['identities'],
            'identity_gates' => $main['identity_gates'],
            'database_owner' => 'SUPREMESETUHUB',
            'connection_mode' => 'shared_central_database',
        ];
    }
}
