<?php
declare(strict_types=1);
require_once __DIR__ . '/php/GlobalSocialMediaCoreContract.php';
/** PHP interoperability facade only; it does not call social-platform APIs. */
final class GlobalSocialMediaCoreManager {
 public static function normalizeResult(array $payload): array { return GlobalSocialMediaCoreContract::fromArray($payload)->toArray(); }
 public static function normalizeJson(string $json): string { return GlobalSocialMediaCoreContract::fromJson($json)->toJson(); }
 public static function isLiveConnectionVerified(array $payload): bool { return GlobalSocialMediaCoreContract::fromArray($payload)->isLiveConnectionVerified(); }
}
