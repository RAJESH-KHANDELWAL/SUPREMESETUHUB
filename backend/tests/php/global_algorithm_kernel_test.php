<?php
declare(strict_types=1);

require_once dirname(__DIR__, 2) . '/php/global_ecosystem/global_php_ecosystem/bootstrap.php';
require_once dirname(__DIR__, 2) . '/php/global_ecosystem/global_php_ecosystem/bada_business_php_ecosystem/bootstrap.php';

use SupremeSetuHub\GlobalEcosystem\PHP\GlobalAlgorithmKernel as Kernel;
use SupremeSetuHub\GlobalEcosystem\PHP\BadaBusiness\BadaBusinessPHPAdapter;

function expect(bool $condition, string $message): void
{
    if (!$condition) {
        fwrite(STDERR, "FAIL: {$message}\n");
        exit(1);
    }
}

expect(Kernel::normalizeIdentifier('  Hello World / API  ') === 'hello-world-api', 'identifier normalization');
expect(
    Kernel::canonicalJson(['z' => 1, 'a' => ['y' => 2, 'x' => 1]])
        === Kernel::canonicalJson(['a' => ['x' => 1, 'y' => 2], 'z' => 1]),
    'canonical JSON key ordering'
);
expect(
    Kernel::stableHash(['b' => 2, 'a' => 1]) === Kernel::stableHash(['a' => 1, 'b' => 2]),
    'stable hash key ordering'
);

$page = Kernel::paginate([10, 20, 30, 40, 50], 2, 2, 3);
expect($page['items'] === [30, 40] && $page['total'] === 5 && $page['total_pages'] === 3, 'bounded pagination');
expect(Kernel::paginate([], 1, 25)['total_pages'] === 0, 'empty pagination');
expect(Kernel::retryDelaySeconds(1) === 1, 'first retry delay');
expect(Kernel::retryDelaySeconds(5) === 16, 'exponential retry delay');
expect(Kernel::retryDelaySeconds(99, 1, 10) === 10, 'retry delay cap');

$clean = Kernel::redact([
    'username' => 'owner',
    'api_key' => 'do-not-log',
    'nested' => ['access_token' => 'secret', 'safe' => 'visible'],
]);
expect($clean['api_key'] === '[REDACTED]', 'top-level secret redaction');
expect($clean['nested']['access_token'] === '[REDACTED]', 'nested secret redaction');
expect($clean['nested']['safe'] === 'visible', 'safe data preserved');

$bada = new BadaBusinessPHPAdapter([
    ['id' => 'digital-dukan', 'name' => 'Digital Dukan', 'type' => 'catalog'],
    ['id' => 'program-alpha', 'name' => 'Business Program', 'type' => 'program'],
]);
expect($bada->catalog()['connected'] === false, 'Bada Business adapter must not claim live connection');
expect(count($bada->search('digital')) === 1, 'Bada Business catalog search');

echo "All global PHP ecosystem tests passed.\n";
