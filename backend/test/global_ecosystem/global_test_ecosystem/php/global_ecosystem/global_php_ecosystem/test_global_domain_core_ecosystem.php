<?php
declare(strict_types=1);

/**
 * Read-only contract test for the singular directory layout of all
 * independent Domain Core provider packages.
 */

$repoRoot = dirname(__DIR__, 7);
$providerRoot = $repoRoot
    . '/backend/core/global_ecosystem/global_core_ecosystem/global_domain_core_ecosystem';

$providers = [
    'abelohost_domain_core_ecosystem',
    'acme_domain_core_ecosystem',
    'afilias_domain_core_ecosystem',
    'afraid_domain_core_ecosystem',
];

$requiredDirectories = ['event', 'model', 'schema', 'service', 'test'];
$obsoleteDirectories = ['events', 'models', 'schemas', 'services', 'tests'];

$failures = [];

foreach ($providers as $provider) {
    $providerPath = $providerRoot . '/' . $provider;

    if (!is_dir($providerPath)) {
        $failures[] = "Missing provider package: {$provider}";
        continue;
    }

    foreach ($requiredDirectories as $directory) {
        if (!is_dir($providerPath . '/' . $directory)) {
            $failures[] = "Missing singular directory: {$provider}/{$directory}";
        }
    }

    foreach ($obsoleteDirectories as $directory) {
        if (is_dir($providerPath . '/' . $directory)) {
            $failures[] = "Obsolete plural directory still exists: {$provider}/{$directory}";
        }
    }
}

if ($failures !== []) {
    foreach ($failures as $failure) {
        fwrite(STDERR, "FAIL: {$failure}" . PHP_EOL);
    }
    exit(1);
}

echo "All Domain Core provider directory layout tests passed." . PHP_EOL;
