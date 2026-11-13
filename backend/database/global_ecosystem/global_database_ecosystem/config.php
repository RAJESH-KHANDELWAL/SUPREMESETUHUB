<?php
declare(strict_types=1);
require_once dirname(__DIR__, 2) . '/config.php';
/** GDE is governed by the main foundation and exposes all five identity DBs. */
if (!function_exists('global_database_ecosystem_config')) {
    function global_database_ecosystem_config(): array
    {
        $main = supreme_main_foundation_config();
        return [
            'id' => 'GLOBAL_DATABASE_ECOSYSTEM',
            'layer' => 'global_database_ecosystem',
            'parent' => 'GLOBAL_ECOSYSTEM',
            'primary_identity' => $main['primary_identity'],
            'identities' => $main['identities'],
            'identity_gates' => $main['identity_gates'],
            'database_topology' => 'ONE_MAIN_PLUS_FOUR_IDENTITY_DATABASES',
            'provider' => 'HOSTINGER_MYSQL_MARIADB',
            'databases' => $main['databases'],
            'wordpress_database' => $main['wordpress_database'],
            'schema_management' => 'explicit_migrations_only',
        ];
    }
}
