<?php
/**
 * PHP-side contract checks for the canonical Backend Android Foundation.
 * Run with: php backend/test/test_backend_android_foundation.php
 */

$root = dirname(__DIR__, 2);
$manager = $root . '/backend/foundation/global_ecosystem/global_foundation_ecosystem/android/manager.py';
$gradle = $root . '/backend/mobile/android/app/build.gradle';

function expect_file(string $path, string $label): void
{
    if (!is_file($path)) {
        fwrite(STDERR, "FAIL: Missing {$label}: {$path}\n");
        exit(1);
    }
}

function expect_match(string $pattern, string $content, string $label): void
{
    if (preg_match($pattern, $content) !== 1) {
        fwrite(STDERR, "FAIL: Android Gradle contract missing {$label}\n");
        exit(1);
    }
}

expect_file($manager, 'Android Foundation manager');
expect_file($gradle, 'Android app Gradle configuration');

$content = file_get_contents($gradle);
if ($content === false) {
    fwrite(STDERR, "FAIL: Unable to read Android Gradle configuration\n");
    exit(1);
}

$checks = [
    '/applicationId\s+[\'"]com\.mainbasefoundation\.android[\'"]/' => 'applicationId',
    '/namespace\s+[\'"]com\.mainbasefoundation\.android[\'"]/' => 'namespace',
    '/compileSdk\s+36\b/' => 'compileSdk 36',
    '/minSdk\s+26\b/' => 'minSdk 26',
    '/targetSdk\s+36\b/' => 'targetSdk 36',
    '/sourceCompatibility\s+JavaVersion\.VERSION_17/' => 'Java 17 source compatibility',
    '/testInstrumentationRunner\s+"androidx\.test\.runner\.AndroidJUnitRunner"/' => 'Android instrumentation test runner',
];

foreach ($checks as $pattern => $label) {
    expect_match($pattern, $content, $label);
}

echo "PASS: Backend Android Foundation contract checks\n";
