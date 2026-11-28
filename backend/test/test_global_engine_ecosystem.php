<?php
declare(strict_types=1);

/**
 * Structural contract tests for the MAIN GLOBAL ENGINE package.
 * The runtime implementation remains in Python; this test does not invent a PHP engine.
 */

function expectGlobalEngine(bool $condition, string $message): void
{
    if (!$condition) {
        fwrite(STDERR, "FAIL: {$message}\n");
        exit(1);
    }
}

$root = dirname(__DIR__, 2) . '/engine/global_ecosystem/global_engine_ecosystem';
$required = ['__init__.py', 'manager.py', 'catalog.py', 'registry.py'];
foreach ($required as $file) {
    expectGlobalEngine(is_file($root . DIRECTORY_SEPARATOR . $file), "required MAIN ENGINE file exists: {$file}");
}

$manager = file_get_contents($root . '/manager.py');
expectGlobalEngine($manager !== false, 'MAIN ENGINE manager is readable');
expectGlobalEngine(str_contains($manager, 'GLOBAL-ENGINE-ECOSYSTEM'), 'manager declares canonical engine identity');
expectGlobalEngine(str_contains($manager, 'PROVIDER_ECOSYSTEMS'), 'manager owns provider ecosystem catalog');

$entrypoint = file_get_contents($root . '/__init__.py');
expectGlobalEngine($entrypoint !== false, 'MAIN ENGINE public entry point is readable');
expectGlobalEngine(str_contains($entrypoint, 'LAYER = "ENGINE"'), 'public entry point identifies ENGINE layer');

echo "All Global Engine Ecosystem PHP structural tests passed.\n";
