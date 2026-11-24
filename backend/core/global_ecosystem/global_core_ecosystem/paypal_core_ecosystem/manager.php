<?php
declare(strict_types=1);
/** PHP interoperability facade; Python remains the canonical Core manager. */
require_once __DIR__ . '/paypal_php_core_ecosystem/PayPalCoreContract.php';
final class PayPalCoreManager
{
    public static function normalizeResult(array $payload): array { return PayPalCoreContract::fromArray($payload)->toArray(); }
    public static function normalizeJson(string $json): string { return PayPalCoreContract::fromJson($json)->toJson(); }
    public static function isLiveConnectionVerified(array $payload): bool { return PayPalCoreContract::fromArray($payload)->isLiveConnectionVerified(); }
}
