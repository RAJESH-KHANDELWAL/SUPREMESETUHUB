<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/config.php';

/** Global Database Ecosystem is a child gate over the central database. */
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
            'provider' => 'HOSTINGER_MARIADB',
            'connection_env_prefix' => 'SUPREME_DB_',
            'connection_mode' => 'shared_central_database',
            'schema_management' => 'explicit_migrations_only',
        ];
    }
}
