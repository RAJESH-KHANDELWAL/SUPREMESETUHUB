<?php
/** PHP structural tests for Backend Global Android Ecosystem. */

$root = dirname(__DIR__, 2);
$managerPath = $root . '/backend/android/global_ecosystem/global_android_ecosystem/manager.py';
$readmePath = $root . '/backend/android/global_ecosystem/global_android_ecosystem/README.md';

foreach (['Backend Android manager' => $managerPath, 'Backend Android README' => $readmePath] as $label => $path) {
    if (!is_file($path)) {
        fwrite(STDERR, "FAIL: Missing {$label}: {$path}\n");
        exit(1);
    }
}

$source = file_get_contents($managerPath);
if ($source === false) {
    fwrite(STDERR, "FAIL: Cannot read Backend Android manager\n");
    exit(1);
}

$checks = [
    '/class\s+GlobalAndroidEcosystemManager\b/' => 'Backend manager class',
    '/def\s+get_manager\s*\(/' => 'Backend manager factory',
    '/STRUCTURE_READY/' => 'Backend structure status',
];

foreach ($checks as $pattern => $label) {
    if (preg_match($pattern, $source) !== 1) {
        fwrite(STDERR, "FAIL: Missing {$label}\n");
        exit(1);
    }
}

echo "Backend Global Android Ecosystem PHP tests passed.\n";
