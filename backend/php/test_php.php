<?php
declare(strict_types=1);

require_once __DIR__ . '/IdentityGate.php';

function expectPhp(bool $condition, string $message): void
{
    if (!$condition) {
        fwrite(STDERR, "FAIL: {$message}\n");
        exit(1);
    }
}

expectPhp(SupremeIdentityGate::normalize(' supremeSetuHub ') === 'SUPREMESETUHUB', 'main identity normalization');
expectPhp(
    SupremeIdentityGate::normalize('DRRAJESHKHANDELWALIBC') === 'DRRAJESHKHANDELWALIBC',
    'brand identity normalization'
);

$scope = SupremeIdentityGate::scope('RAJESHKHANDELWALOFFICIAL');
expectPhp($scope['sql'] === 'identity_code = :identity_code', 'safe SQL scope expression');
expectPhp(
    $scope['params']['identity_code'] === 'RAJESHKHANDELWALOFFICIAL',
    'identity scope parameter'
);

$rejectedUnknownIdentity = false;
try {
    SupremeIdentityGate::normalize('UNKNOWN_IDENTITY');
} catch (InvalidArgumentException) {
    $rejectedUnknownIdentity = true;
}
expectPhp($rejectedUnknownIdentity, 'unknown identity rejected');

$rejectedUnsafeColumn = false;
try {
    SupremeIdentityGate::scope('SUPREMESETUHUB', 'identity_code; DROP TABLE users');
} catch (InvalidArgumentException) {
    $rejectedUnsafeColumn = true;
}
expectPhp($rejectedUnsafeColumn, 'unsafe SQL column rejected');

$rejectedCrossIdentity = false;
try {
    SupremeIdentityGate::assertSameIdentity('RAJESHKHANDELWAL', 'DRRAJESHKHANDELWALIBC');
} catch (RuntimeException) {
    $rejectedCrossIdentity = true;
}
expectPhp($rejectedCrossIdentity, 'cross-identity access rejected');

echo "All PHP foundation tests passed.\n";
