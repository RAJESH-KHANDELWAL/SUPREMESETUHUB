<?php
declare(strict_types=1);

/**
 * MAIN BASE FOUNDATION — shared database configuration helpers.
 * Secrets are loaded from environment variables or a private PHP config file
 * located outside the public web root. Never commit real credentials.
 */

$privateConfigPath = supreme_database_private_config_path();
if ($privateConfigPath !== null && is_file($privateConfigPath)) {
    $privateConfig = require $privateConfigPath;
    if (is_array($privateConfig)) {
        $GLOBALS['SUPREME_DB_PRIVATE_VALUES'] = $privateConfig;
    }
}

if (!function_exists('supreme_database_private_config_path')) {
    function supreme_database_private_config_path(): ?string
    {
        $configured = getenv('SUPREME_DB_PRIVATE_CONFIG');
        if ($configured !== false && trim($configured) !== '') {
            return trim($configured);
        }
        return null;
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
        if (is_array($private) && isset($private[$name]) && trim((string) $private[$name]) !== '') {
            return trim((string) $private[$name]);
        }
        return $default;
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

/**
 * SUPREMESETUHUB — one central database with one primary identity and four
 * identity gates. This returns configuration only; it does not connect to
 * MySQL or create/modify database tables.
 *
 * Set SUPREME_DB_HOST to the exact MySQL hostname shown in Hostinger hPanel.
 * Never put the database password in this source file.
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

        return [
            'system' => 'SUPREMESETUHUB',
            'architecture' => 'ONE_DATABASE_ONE_PRIMARY_FOUR_IDENTITY_GATES',
            'primary_identity' => 'SUPREMESETUHUB',
            'identity_gates' => [
                'RAJESHKHANDELWALOFFICIAL',
                'RAJESHKHANDELWAL',
                'DRRAJESHKHANDELWALIBCOFFICIAL',
                'DRRAJESHKHANDELWALIBC',
            ],
            'identities' => $identities,

            'database' => [
                'driver' => 'mysql',
                'host' => supreme_database_env('SUPREME_DB_HOST', ''),
                'name' => supreme_database_env(
                    'SUPREME_DB_NAME',
                    'u664492673_SUPREMESETUHUB'
                ),
                'username' => supreme_database_env(
                    'SUPREME_DB_USER',
                    'u664492673_SUPREMESETUHUB'
                ),
                'password' => supreme_database_env('SUPREME_DB_PASSWORD', ''),
                'port' => (int) supreme_database_env('SUPREME_DB_PORT', '3306'),
                'charset' => 'utf8mb4',
                'connect_timeout' => 10,
            ],

            // Application entry points that may use the central identity system.
            'gates' => [
                'GITHUB',
                'WEBSITE',
                'WORDPRESS',
                'AI',
                'API',
                'APP',
                'BUSINESS',
                'ADMIN',
                'GLOBAL',
                'SUPREME',
            ],
        ];
    }
}
