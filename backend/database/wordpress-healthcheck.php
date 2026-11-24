<?php
declare(strict_types=1);

/**
 * Read-only WordPress database connectivity check.
 *
 * Run from the deployed repository root:
 *   php backend/database/wordpress-healthcheck.php
 *
 * CLI-only by design: it cannot be opened over HTTP. It never prints
 * credentials and performs SELECT-only checks; it does not alter tables/data.
 */

if (PHP_SAPI !== 'cli') {
    http_response_code(404);
    exit("Not found.\n");
}

require_once __DIR__ . '/database.php';

try {
    $config = supreme_wordpress_database_connection_config();
    $pdo = supreme_wordpress_database_connection();

    $database = $pdo->query('SELECT DATABASE()')->fetchColumn();
    if (!is_string($database) || $database !== $config['database']) {
        throw new RuntimeException('Connected database does not match configured WordPress database.');
    }

    $prefix = (string) ($config['table_prefix'] ?? 'wp_');
    $stmt = $pdo->prepare(
        'SELECT COUNT(*) FROM information_schema.tables
         WHERE table_schema = DATABASE() AND table_name LIKE :table_pattern'
    );
    $stmt->execute(['table_pattern' => addcslashes($prefix, '_%\\\\') . '%']);
    $tableCount = (int) $stmt->fetchColumn();

    echo "WORDPRESS_DB_CONFIG: PASS\n";
    echo "WORDPRESS_DB_CONNECTION: PASS\n";
    echo "DATABASE_IDENTITY_MATCH: PASS\n";
    echo "WORDPRESS_PREFIX_TABLES_FOUND: " . ($tableCount > 0 ? "YES" : "NO") . "\n";
    echo "PREFIX_TABLE_COUNT: " . $tableCount . "\n";
    echo "READ_ONLY_CHECK: PASS\n";
    exit(0);
} catch (Throwable $error) {
    // Deliberately avoid echoing DSNs, usernames, passwords, or exception details.
    fwrite(STDERR, "WORDPRESS_DB_HEALTHCHECK: FAIL\n");
    fwrite(STDERR, "REASON: " . get_class($error) . "\n");
    fwrite(STDERR, "DETAIL: Check private Hostinger DB settings and PHP PDO MySQL availability.\n");
    exit(1);
}
