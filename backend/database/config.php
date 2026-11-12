<?php
declare(strict_types=1);

/**
 * MAIN BASE FOUNDATION — shared database configuration helpers.
 * Secrets are read from the runtime environment, never from source files.
 */

if (!function_exists('supreme_database_env')) {
    function supreme_database_env(string $name, ?string $default = null): ?string
    {
        $value = getenv($name);
        if ($value === false || trim($value) === '') {
            return $default;
        }
        return trim($value);
    }
}

if (!function_exists('supreme_database_config')) {
    /**
     * Build a connection config from a dedicated environment prefix.
     * The GDE connection never falls back to WordPress credentials.
     */
    function supreme_database_config(string $prefix = 'GDE_DB_'): array
    {
        $config = [
            'host' => supreme_database_env($prefix . 'HOST'),
            'database' => supreme_database_env($prefix . 'NAME'),
            'username' => supreme_database_env($prefix . 'USER'),
            'password' => supreme_database_env($prefix . 'PASSWORD'),
            'port' => (int) supreme_database_env($prefix . 'PORT', '3306'),
            'connect_timeout' => (int) supreme_database_env($prefix . 'CONNECT_TIMEOUT', '10'),
            'ssl_required' => filter_var(
                supreme_database_env($prefix . 'SSL_REQUIRED', 'true'),
                FILTER_VALIDATE_BOOLEAN
            ),
            'ssl_ca' => supreme_database_env($prefix . 'SSL_CA'),
        ];

        $missing = [];
        foreach (['host', 'database', 'username', 'password'] as $key) {
            if ($config[$key] === null || $config[$key] === '') {
                $missing[] = $prefix . strtoupper($key === 'username' ? 'USER' : ($key === 'database' ? 'NAME' : $key));
            }
        }
        if ($missing !== []) {
            throw new InvalidArgumentException('Missing database settings: ' . implode(', ', $missing));
        }
        if ($config['port'] < 1 || $config['port'] > 65535) {
            throw new InvalidArgumentException($prefix . 'PORT must be between 1 and 65535');
        }
        if ($config['connect_timeout'] < 1) {
            throw new InvalidArgumentException($prefix . 'CONNECT_TIMEOUT must be positive');
        }

        // Protect the primary WordPress database. The separately selected
        // second Hostinger database may be assigned to GDE by the owner.
        $primaryWordPressDb = supreme_database_env('WORDPRESS_DB_NAME');
        if ($prefix === 'GDE_DB_' && $primaryWordPressDb !== null
            && hash_equals($primaryWordPressDb, (string) $config['database'])) {
            throw new InvalidArgumentException(
                'GDE_DB_NAME must not point to the primary WordPress database.'
            );
        }

        if ($config['ssl_required'] && !$config['ssl_ca']) {
            throw new InvalidArgumentException(
                $prefix . 'SSL_CA is required while SSL_REQUIRED is enabled.'
            );
        }

        return $config;
    }
}
