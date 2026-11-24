<?php
declare(strict_types=1);

/**
 * GITHUB-SUPREME — Host and domain registry entry point.
 * PHP 8.1+. This page reports configuration status only; it never prints secrets.
 */
require_once __DIR__ . '/core/Registry.php';

use GithubSupreme\Registry;

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store');

try {
    $registry = Registry::fromDirectory(__DIR__);
    http_response_code(200);
    echo json_encode([
        'system' => 'GITHUB-SUPREME',
        'status' => 'initialized',
        'hosts_configured' => $registry->configuredHostCount(),
        'host_slots' => $registry->hostSlotCount(),
        'domains' => $registry->domains(),
        'secrets_exposed' => false,
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
} catch (Throwable $error) {
    http_response_code(503);
    echo json_encode([
        'system' => 'GITHUB-SUPREME',
        'status' => 'configuration_required',
        'message' => 'Registry configuration is missing or invalid.',
        'secrets_exposed' => false,
    ], JSON_PRETTY_PRINT);
}
