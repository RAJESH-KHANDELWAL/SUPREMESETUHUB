<?php
declare(strict_types=1);

/**
 * Shared PDO connection for the SUPREME digital-design marketplace.
 * Credentials must be injected by the hosting environment.
 */
final class Database
{
    public static function connection(): PDO
    {
        $host = self::requiredEnv('SUPREME_DB_HOST');
        $port = self::optionalEnv('SUPREME_DB_PORT', '3306');
        $name = self::requiredEnv('SUPREME_DB_NAME');
        $user = self::requiredEnv('SUPREME_DB_USER');
        $password = self::requiredEnv('SUPREME_DB_PASSWORD');

        if (!ctype_digit($port) || (int) $port < 1 || (int) $port > 65535) {
            throw new RuntimeException('SUPREME_DB_PORT must be a valid TCP port.');
        }

        $dsn = sprintf(
            'mysql:host=%s;port=%s;dbname=%s;charset=utf8mb4',
            $host,
            $port,
            $name
        );

        return new PDO($dsn, $user, $password, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
            PDO::ATTR_STRINGIFY_FETCHES => false,
        ]);
    }

    private static function requiredEnv(string $key): string
    {
        $value = getenv($key);
        if ($value === false || trim($value) === '') {
            throw new RuntimeException('Missing required server environment variable: ' . $key);
        }
        return trim($value);
    }

    private static function optionalEnv(string $key, string $default): string
    {
        $value = getenv($key);
        return ($value === false || trim($value) === '') ? $default : trim($value);
    }
}
