<?php
/** PHP structural tests for Frontend Global Android Ecosystem. */

$root = dirname(__DIR__, 2);
$managerPath = $root . '/frontend/android/global_ecosystem/global_android_ecosystem/manager.py';
$readmePath = $root . '/frontend/android/global_ecosystem/global_android_ecosystem/README.md';

foreach (['Frontend Android manager' => $managerPath, 'Frontend Android README' => $readmePath] as $label => $path) {
    if (!is_file($path)) {
        fwrite(STDERR, "FAIL: Missing {$label}: {$path}\n");
        exit(1);
    }
}

$source = file_get_contents($managerPath);
if ($source === false) {
    fwrite(STDERR, "FAIL: Cannot read Frontend Android manager\n");
    exit(1);
}

$checks = [
    '/class\s+FrontendGlobalAndroidEcosystemManager\b/' => 'Frontend manager class',
    '/def\s+get_manager\s*\(/' => 'Frontend manager factory',
    '/STRUCTURE_READY/' => 'Frontend structure status',
];

foreach ($checks as $pattern => $label) {
    if (preg_match($pattern, $source) !== 1) {
        fwrite(STDERR, "FAIL: Missing {$label}\n");
        exit(1);
    }
}

echo "Frontend Global Android Ecosystem PHP tests passed.\n";
