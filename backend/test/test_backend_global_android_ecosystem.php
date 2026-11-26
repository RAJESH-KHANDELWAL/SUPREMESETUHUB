<?php
/**
 * PHP-side structural checks for Global Android Ecosystem.
 * Run with: php backend/test/test_backend_global_android_ecosystem.php
 */

$root = dirname(__DIR__, 2);
$package = $root . '/backend/android/global_ecosystem/global_android_ecosystem';
$manager = $package . '/manager.py';
$readme = $package . '/README.md';
$init = $package . '/__init__.py';
$foundationManager = $root . '/backend/foundation/global_ecosystem/global_foundation_ecosystem/android/manager.py';

$required = [
    'Global Android Ecosystem manager' => $manager,
    'Global Android Ecosystem README' => $readme,
    'Global Android Ecosystem package initializer' => $init,
    'Canonical Android Foundation manager' => $foundationManager,
];

foreach ($required as $label => $path) {
    if (!is_file($path)) {
        fwrite(STDERR, "FAIL: Missing {$label}: {$path}\n");
        exit(1);
    }
}

$managerContent = file_get_contents($manager);
$readmeContent = file_get_contents($readme);
if ($managerContent === false || $readmeContent === false) {
    fwrite(STDERR, "FAIL: Unable to read Android ecosystem source files\n");
    exit(1);
}

$managerChecks = [
    '/class\s+GlobalAndroidEcosystemManager\b/' => 'GlobalAndroidEcosystemManager class',
    '/def\s+get_manager\s*\(/' => 'get_manager factory',
    '/AndroidFoundationManager/' => 'Foundation manager delegation',
    '/GLOBAL_ANDROID_ECOSYSTEM/' => 'ecosystem identity',
];

foreach ($managerChecks as $pattern => $label) {
    if (preg_match($pattern, $managerContent) !== 1) {
        fwrite(STDERR, "FAIL: Missing {$label}\n");
        exit(1);
    }
}

if (strpos($readmeContent, 'backend/mobile/android') === false) {
    fwrite(STDERR, "FAIL: README does not identify the canonical Android project\n");
    exit(1);
}

echo "PASS: Global Android Ecosystem structural checks\n";
