<?php
declare(strict_types=1);
require_once dirname(__DIR__, 2) . '/config.php';

/** GDE uses the same single physical DB and four logical identity gates. */
if (!function_exists('global_database_ecosystem_config')) {
    function global_database_ecosystem_config(): array
    {
        $main = supreme_main_foundation_config();
        return [
            'id' => 'GLOBAL_DATABASE_ECOSYSTEM',
            'layer' => 'global_database_ecosystem',
            'parent' => 'GLOBAL_ECOSYSTEM',
            'database_topology' => 'ONE_PHYSICAL_DATABASE_FOUR_LOGICAL_IDENTITY_GATES',
            'provider' => 'HOSTINGER_MYSQL_MARIADB',
            'primary_identity' => $main['primary_identity'],
            'identities' => $main['identities'],
            'identity_gates' => $main['identity_gates'],
            'database' => $main['database'],
            'databases' => $main['databases'],
            'wordpress_database' => $main['wordpress_database'],
            'schema_management' => 'explicit_migrations_only',
        ];
    }
}
