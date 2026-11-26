<?php
/**
 * PHP structural checks for Backend Global Android Ecosystem.
 * Run with: php backend/test/test_global_android_ecosystem.php
 */

$root = dirname(__DIR__, 2);
$backendManager = $root . '/backend/android/global_ecosystem/global_android_ecosystem/manager.py';
$frontendManager = $root . '/frontend/android/global_ecosystem/global_android_ecosystem/manager.py';
$backendReadme = $root . '/backend/android/global_ecosystem/global_android_ecosystem/README.md';
$frontendReadme = $root . '/frontend/android/global_ecosystem/global_android_ecosystem/README.md';

foreach ([
    'Backend Android manager' => $backendManager,
    'Frontend Android manager' => $frontendManager,
    'Backend Android README' => $backendReadme,
    'Frontend Android README' => $frontendReadme,
] as $label => $path) {
    if (!is_file($path)) {
        fwrite(STDERR, "FAIL: Missing {$label}: {$path}\n");
        exit(1);
    }
}

$backendContent = file_get_contents($backendManager);
$frontendContent = file_get_contents($frontendManager);
if ($backendContent === false || $frontendContent === false) {
    fwrite(STDERR, "FAIL: Unable to read Android manager files\n");
    exit(1);
}

foreach ([
    '/class\s+GlobalAndroidEcosystemManager\b/' => 'Backend manager class',
    '/def\s+get_manager\s*\(/' => 'Backend manager factory',
    '/STRUCTURE_READY/' => 'Backend structure status',
] as $pattern => $label) {
    if (preg_match($pattern, $backendContent) !== 1) {
        fwrite(STDERR, "FAIL: Missing {$label}\n");
        exit(1);
    }
}

foreach ([
    '/class\s+FrontendGlobalAndroidEcosystemManager\b/' => 'Frontend manager class',
    '/def\s+get_manager\s*\(/' => 'Frontend manager factory',
    '/STRUCTURE_READY/' => 'Frontend structure status',
] as $pattern => $label) {
    if (preg_match($pattern, $frontendContent) !== 1) {
        fwrite(STDERR, "FAIL: Missing {$label}\n");
        exit(1);
    }
}

echo "PASS: Global Android ecosystem structural checks\n";
