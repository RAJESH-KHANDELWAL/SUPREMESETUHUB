<?php
declare(strict_types=1);
require_once __DIR__ . '/shopify_php_core_ecosystem/ShopifyCoreContract.php';
/** PHP metadata facade only; no OAuth or Shopify API transport. */
final class ShopifyCoreManager {
 public static function normalizeResult(array $payload): array { return ShopifyCoreContract::fromArray($payload)->toArray(); }
 public static function normalizeJson(string $json): string { return ShopifyCoreContract::fromJson($json)->toJson(); }
 public static function isLiveConnectionVerified(array $payload): bool { return ShopifyCoreContract::fromArray($payload)->isLiveConnectionVerified(); }
}
