<?php
declare(strict_types=1);

require_once __DIR__ . '/bootstrap.php';

use SupremeSetuHub\GlobalEcosystem\PHP\GlobalAlgorithmKernel as Kernel;

function expectGlobalPhp(bool $condition, string $message): void
{
    if (!$condition) {
        fwrite(STDERR, "FAIL: {$message}\n");
        exit(1);
    }
}

expectGlobalPhp(
    Kernel::normalizeIdentifier('  Hello World / API  ') === 'hello-world-api',
    'identifier normalization'
);
expectGlobalPhp(
    Kernel::canonicalJson(['z' => 1, 'a' => ['y' => 2, 'x' => 1]])
        === Kernel::canonicalJson(['a' => ['x' => 1, 'y' => 2], 'z' => 1]),
    'canonical JSON key ordering'
);
expectGlobalPhp(
    Kernel::stableHash(['b' => 2, 'a' => 1]) === Kernel::stableHash(['a' => 1, 'b' => 2]),
    'stable hash key ordering'
);

$page = Kernel::paginate([10, 20, 30, 40, 50], 2, 2, 3);
expectGlobalPhp(
    $page['items'] === [30, 40] && $page['total'] === 5 && $page['total_pages'] === 3,
    'bounded pagination'
);
expectGlobalPhp(Kernel::paginate([], 1, 25)['total_pages'] === 0, 'empty pagination');
expectGlobalPhp(Kernel::retryDelaySeconds(1) === 1, 'first retry delay');
expectGlobalPhp(Kernel::retryDelaySeconds(5) === 16, 'exponential retry delay');
expectGlobalPhp(Kernel::retryDelaySeconds(99, 1, 10) === 10, 'retry delay cap');

$clean = Kernel::redact([
    'username' => 'owner',
    'api_key' => 'do-not-log',
    'nested' => ['access_token' => 'secret', 'safe' => 'visible'],
]);
expectGlobalPhp($clean['api_key'] === '[REDACTED]', 'top-level secret redaction');
expectGlobalPhp($clean['nested']['access_token'] === '[REDACTED]', 'nested secret redaction');
expectGlobalPhp($clean['nested']['safe'] === 'visible', 'safe data preserved');

echo "All GLOBAL PHP ECOSYSTEM tests passed.\n";
