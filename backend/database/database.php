<?php
declare(strict_types=1);

require_once __DIR__ . '/config.php';

/**
 * SUPREMESETUHUB central PDO connection factory.
 * All five identities/gates resolve to the same owner-configured database.
 * Requiring this file does not connect or alter schema/data.
 */
if (!function_exists('supreme_database_connect')) {
    function supreme_database_connect(array $config): PDO
    {
        // Accept either the normalized connection shape or the nested
        // "database" section returned by supreme_main_foundation_config().
        if (isset($config['name']) && !isset($config['database'])) {
            $config['database'] = $config['name'];
        }

        foreach (['host', 'database', 'username', 'password', 'port'] as $key) {
            if (!array_key_exists($key, $config) || $config[$key] === null || $config[$key] === '') {
                throw new InvalidArgumentException('Missing database connection field: ' . $key);
            }
        }

        $dsn = sprintf(
            'mysql:host=%s;port=%d;dbname=%s;charset=utf8mb4',
            $config['host'],
            (int) $config['port'],
            $config['database']
        );

        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
            PDO::ATTR_TIMEOUT => max(1, (int) ($config['connect_timeout'] ?? 10)),
        ];

        if (!empty($config['ssl_required'])) {
            if (empty($config['ssl_ca']) || !is_readable($config['ssl_ca'])) {
                throw new RuntimeException('A readable database TLS CA certificate is required.');
            }
            if (!defined('PDO::MYSQL_ATTR_SSL_CA')) {
                throw new RuntimeException('PDO MySQL TLS support is unavailable in this PHP runtime.');
            }
            $options[constant('PDO::MYSQL_ATTR_SSL_CA')] = $config['ssl_ca'];
            if (defined('PDO::MYSQL_ATTR_SSL_VERIFY_SERVER_CERT')) {
                $options[constant('PDO::MYSQL_ATTR_SSL_VERIFY_SERVER_CERT')] = true;
            }
        }

        return new PDO($dsn, (string) $config['username'], (string) $config['password'], $options);
    }
}

if (!function_exists('supreme_main_database_connection_config')) {
    /** Return the one central SUPREMESETUHUB connection configuration. */
    function supreme_main_database_connection_config(): array
    {
        $main = supreme_main_foundation_config();
        $db = $main['database'];
        return [
            'host' => $db['host'],
            'database' => $db['name'],
            'username' => $db['username'],
            'password' => $db['password'],
            'port' => $db['port'],
            'connect_timeout' => $db['connect_timeout'] ?? 10,
            'charset' => $db['charset'] ?? 'utf8mb4',
            'primary_identity' => $main['primary_identity'],
            'identities' => $main['identities'],
        ];
    }
}

if (!function_exists('supreme_main_database_connection')) {
    /** Open/reuse the one central database connection. */
    function supreme_main_database_connection(): PDO
    {
        static $connection = null;
        if ($connection instanceof PDO) {
            return $connection;
        }
        $connection = supreme_database_connect(supreme_main_database_connection_config());
        return $connection;
    }
}
