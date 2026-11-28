<?php
declare(strict_types=1);
/** Thin PHP interoperability facade; Python owns catalog and orchestration logic. */
final class GlobalStorageCoreManager
{
    public static function sanitizeResult(array $payload): array
    {
        foreach (['token','access_token','refresh_token','client_secret','api_key','secret','credentials','password','private_key'] as $key) { unset($payload[$key]); }
        $payload['live_connection_verified'] = false;
        $payload['storage_operations_performed'] = 0;
        $payload['api_transport_in_core'] = false;
        return $payload;
    }
    public static function encodeResult(array $payload): string
    {
        return json_encode(self::sanitizeResult($payload), JSON_THROW_ON_ERROR | JSON_UNESCAPED_SLASHES);
    }
}
