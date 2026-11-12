<?php
declare(strict_types=1);

/** Global Database Ecosystem identity and runtime boundary. */
if (!function_exists('global_database_ecosystem_config')) {
    function global_database_ecosystem_config(): array
    {
        return [
            'id' => 'GLOBAL_DATABASE_ECOSYSTEM',
            'layer' => 'global_database_ecosystem',
            'parent' => 'GLOBAL_ECOSYSTEM',
            'provider' => 'HOSTINGER_MARIADB',
            'connection_env_prefix' => 'GDE_DB_',
            'schema_management' => 'explicit_migrations_only',
        ];
    }
}
