<?php
declare(strict_types=1);
/** PHP interoperability facade for Adobe Core contracts; no provider API calls. */
require_once __DIR__ . '/php/AdobeCoreContract.php';
final class AdobeCoreManager {
    public static function normalizeResult(array $payload): array {
        return AdobeCoreContract::fromArray($payload)->toArray();
    }
    public static function normalizeJson(string $json): string {
        return AdobeCoreContract::fromJson($json)->toJson();
    }
    public static function isLiveConnectionVerified(array $payload): bool {
        return AdobeCoreContract::fromArray($payload)->isLiveConnectionVerified();
    }
}
