<?php
declare(strict_types=1);
/** PHP interoperability facade; Python remains the canonical Stripe Core manager. */
require_once __DIR__ . '/stripe_php_core_ecosystem/StripeCoreContract.php';
final class StripeCoreManager {
 public static function normalizeResult(array $payload): array { return StripeCoreContract::fromArray($payload)->toArray(); }
 public static function normalizeJson(string $json): string { return StripeCoreContract::fromJson($json)->toJson(); }
 public static function isLiveConnectionVerified(array $payload): bool { return StripeCoreContract::fromArray($payload)->isLiveConnectionVerified(); }
}
