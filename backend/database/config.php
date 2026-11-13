<?php
declare(strict_types=1);

/**
 * SUPREMESETUHUB MAIN BASE FOUNDATION.
 *
 * Database topology:
 *   1. SUPREMESETUHUB — central/main database.
 *   2. RAJESHKHANDELWALOFFICIAL — dedicated identity database.
 *   3. RAJESHKHANDELWAL — dedicated identity database.
 *   4. DRRAJESHKHANDELWALIBCOFFICIAL — dedicated identity database.
 *   5. DRRAJESHKHANDELWALIBC — dedicated identity database.
 *
 * The four identity gates remain under the central foundation, but each gate
 * has its own database and credentials. This file only builds configuration;
 * it does not connect to MySQL or create databases/tables.
 *
 * Secrets must be supplied through environment variables or a private PHP
 * config file outside the public web root. Never commit real credentials.
 */

if (!function_exists('supreme_database_private_config_path')) {
    function supreme_database_private_config_path(): ?string
    {
        // Optional explicit override (for hosting environments that support it).
        $configured = getenv('SUPREME_DB_PRIVATE_CONFIG');
        if ($configured !== false && trim($configured) !== '') {
            return trim($configured);
        }

        // Default for: public_html/backend/database/config.php
        // Place supreme-db-private.php one level above public_html.
        $defaultPath = dirname(__DIR__, 3) . DIRECTORY_SEPARATOR . 'supreme-db-private.php';
        return $defaultPath;
    }
}

$privateConfigPath = supreme_database_private_config_path();
if ($privateConfigPath !== null && is_file($privateConfigPath)) {
    $privateConfig = require $privateConfigPath;
    if (is_array($privateConfig)) {
        $GLOBALS['SUPREME_DB_PRIVATE_VALUES'] = $privateConfig;
    }
}

if (!function_exists('supreme_database_env')) {
    function supreme_database_env(string $name, ?string $default = null): ?string
    {
        $value = getenv($name);
        if ($value !== false && trim($value) !== '') {
            return trim($value);
        }

        $private = $GLOBALS['SUPREME_DB_PRIVATE_VALUES'] ?? [];
        if (
            is_array($private)
            && isset($private[$name])
            && trim((string) $private[$name]) !== ''
        ) {
            return trim((string) $private[$name]);
        }

        return $default;
    }
}

if (!function_exists('supreme_database_config')) {
    /**
     * Build a strict database config from a dedicated environment prefix.
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
                $missing[] = $prefix . strtoupper(
                    $key === 'username' ? 'USER' : ($key === 'database' ? 'NAME' : $key)
                );
            }
        }

        if ($missing !== []) {
            throw new InvalidArgumentException(
                'Missing database settings: ' . implode(', ', $missing)
            );
        }
        if ($config['port'] < 1 || $config['port'] > 65535) {
            throw new InvalidArgumentException($prefix . 'PORT must be between 1 and 65535');
        }
        if ($config['connect_timeout'] < 1) {
            throw new InvalidArgumentException($prefix . 'CONNECT_TIMEOUT must be positive');
        }

        $primaryWordPressDb = supreme_database_env('WORDPRESS_DB_NAME');
        if (
            $prefix === 'GDE_DB_'
            && $primaryWordPressDb !== null
            && hash_equals($primaryWordPressDb, (string) $config['database'])
        ) {
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

if (!function_exists('supreme_wordpress_database_config')) {
    /**
     * Build the separate connection config for the existing WordPress database.
     * This is intentionally separate from the SUPREMESETUHUB central database.
     */
    function supreme_wordpress_database_config(): array
    {
        $config = [
            'identity' => 'WORDPRESS',
            'driver' => 'mysql',
            'host' => supreme_database_env('WORDPRESS_DB_HOST', ''),
            'name' => supreme_database_env('WORDPRESS_DB_NAME', ''),
            // Dedicated Hostinger account with SELECT-only grants; never use the site's own DB user.
            'username' => supreme_database_env('WORDPRESS_READONLY_DB_USER', ''),
            'password' => supreme_database_env('WORDPRESS_READONLY_DB_PASSWORD'),
            // Username of the site's existing application account, used only
            // to reject accidental reuse of that account for the connector.
            'primary_username' => supreme_database_env('WORDPRESS_PRIMARY_DB_USER', ''),
            'port' => (int) supreme_database_env('WORDPRESS_DB_PORT', '3306'),
            'charset' => 'utf8mb4',
            'table_prefix' => supreme_database_env('WORDPRESS_TABLE_PREFIX', 'wp_'),
            'connect_timeout' => (int) supreme_database_env('WORDPRESS_DB_CONNECT_TIMEOUT', '10'),
            'ssl_required' => filter_var(
                supreme_database_env('WORDPRESS_DB_SSL_ENABLED', 'false'),
                FILTER_VALIDATE_BOOLEAN
            ),
            'ssl_ca' => supreme_database_env('WORDPRESS_DB_SSL_CA'),
        ];

        $missing = [];
        foreach (['host', 'name', 'username', 'password', 'primary_username'] as $key) {
            if ($config[$key] === null || $config[$key] === '') {
                $missing[] = match ($key) {
                    'username' => 'WORDPRESS_READONLY_DB_USER',
                    'password' => 'WORDPRESS_READONLY_DB_PASSWORD',
                    'primary_username' => 'WORDPRESS_PRIMARY_DB_USER',
                    'name' => 'WORDPRESS_DB_NAME',
                    default => 'WORDPRESS_DB_HOST',
                };
            }
        }
        if (
            $config['username'] !== ''
            && $config['primary_username'] !== ''
            && hash_equals($config['primary_username'], $config['username'])
        ) {
            $missing[] = 'WORDPRESS_READONLY_DB_USER_MUST_DIFFER_FROM_PRIMARY';
        }

        if ($config['port'] < 1 || $config['port'] > 65535) {
            $missing[] = 'WORDPRESS_DB_PORT_INVALID';
        }
        if ($config['connect_timeout'] < 1) {
            $missing[] = 'WORDPRESS_DB_CONNECT_TIMEOUT_INVALID';
        }
        if ($config['ssl_required'] && !$config['ssl_ca']) {
            $missing[] = 'WORDPRESS_DB_SSL_CA';
        }

        $config['missing_settings'] = $missing;
        $config['configured'] = $missing === [];
        return $config;
    }
}

/**
 * Return one physical SUPREMESETUHUB database and four logical identity gates.
 * Every identity gate is isolated by identity scope inside this same database.
 */
if (!function_exists('supreme_main_foundation_config')) {
    function supreme_main_foundation_config(): array
    {
        $identities = [
            'SUPREMESETUHUB',
            'RAJESHKHANDELWALOFFICIAL',
            'RAJESHKHANDELWAL',
            'DRRAJESHKHANDELWALIBCOFFICIAL',
            'DRRAJESHKHANDELWALIBC',
        ];

        $centralDatabase = [
            'identity' => 'SUPREMESETUHUB',
            'driver' => 'mysql',
            'host' => supreme_database_env('SUPREME_DB_HOST', ''),
            'name' => supreme_database_env('SUPREME_DB_NAME', 'u664492673_SUPREMESETUHUB'),
            'username' => supreme_database_env('SUPREME_DB_USER', 'u664492673_SUPREMESETUHUB'),
            'password' => supreme_database_env('SUPREME_DB_PASSWORD', ''),
            'port' => (int) supreme_database_env('SUPREME_DB_PORT', '3306'),
            'charset' => 'utf8mb4',
            'connect_timeout' => (int) supreme_database_env('SUPREME_DB_CONNECT_TIMEOUT', '10'),
        ];

        $identityGates = [];
        foreach (array_slice($identities, 1) as $identity) {
            $identityGates[$identity] = [
                'identity' => $identity,
                'gate_type' => 'LOGICAL_IDENTITY_GATE',
                'storage_database' => 'SUPREMESETUHUB',
                'scope_column' => 'identity_code',
                'scope_value' => $identity,
                'separate_physical_database' => false,
            ];
        }

        return [
            'system' => 'SUPREMESETUHUB',
            'architecture' => 'ONE_PHYSICAL_DATABASE_FOUR_LOGICAL_IDENTITY_GATES',
            'primary_identity' => 'SUPREMESETUHUB',
            'identities' => $identities,
            'identity_gates' => $identityGates,
            'database' => $centralDatabase,
            // Compatibility map: all five identities intentionally resolve to the same DB.
            'databases' => array_fill_keys($identities, $centralDatabase),
            'wordpress_database' => supreme_wordpress_database_config(),
            'gates' => [
                'GITHUB', 'WEBSITE', 'WORDPRESS', 'AI', 'API',
                'APP', 'BUSINESS', 'ADMIN', 'GLOBAL', 'SUPREME',
            ],
        ];
    }
}
