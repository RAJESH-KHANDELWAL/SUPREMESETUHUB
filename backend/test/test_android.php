<?php
/**
 * PHP structural checks for the independent Android roots.
 * Run with: php backend/test/test_android.php
 */

$root = dirname(__DIR__, 2);
$required = [
    'Backend Android README' => $root . '/backend/android/README.md',
    'Backend Android manager' => $root . '/backend/android/global_ecosystem/global_android_ecosystem/manager.py',
    'Frontend Android README' => $root . '/frontend/android/README.md',
    'Frontend Android manager' => $root . '/frontend/android/global_ecosystem/global_android_ecosystem/manager.py',
];

foreach ($required as $label => $path) {
    if (!is_file($path)) {
        fwrite(STDERR, "FAIL: Missing {$label}: {$path}\n");
        exit(1);
    }
}

if (is_dir($root . '/backend/mobile/android')) {
    fwrite(STDERR, "FAIL: Legacy backend/mobile/android project should not be required\n");
    exit(1);
}

echo "PASS: Android root structure checks\n";
