<?php
declare(strict_types=1);
require_once __DIR__ . '/php/AtlassianCoreContract.php';
/** PHP interoperability facade; Python is the canonical metadata manager. */
final class AtlassianCoreManager {
 public static function normalizeResult(array $payload): array { return AtlassianCoreContract::normalize($payload); }
 public static function normalizeJson(string $json): string { $payload=json_decode($json,true,512,JSON_THROW_ON_ERROR); return json_encode(self::normalizeResult($payload),JSON_THROW_ON_ERROR|JSON_UNESCAPED_SLASHES); }
 public static function isLiveConnectionVerified(array $payload): bool { return ($payload['live_connection_verified']??false)===true; }
}
