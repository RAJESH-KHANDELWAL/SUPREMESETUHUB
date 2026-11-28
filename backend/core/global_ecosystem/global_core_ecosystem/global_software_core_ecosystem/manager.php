<?php
declare(strict_types=1);
/** PHP interoperability facade; Python remains the canonical catalog manager. */
final class GlobalSoftwareCoreManager
{
    public static function normalizeResult(array $payload): array
    {
        $blocked = ['token', 'access_token', 'refresh_token', 'client_secret', 'api_key', 'password'];
        foreach ($blocked as $key) { unset($payload[$key]); }
        $payload['api_transport_in_core'] = false;
        $payload['live_connection_verified'] = false;
        return $payload;
    }
    public static function normalizeJson(string $json): string
    {
        $payload = json_decode($json, true, 512, JSON_THROW_ON_ERROR);
        if (!is_array($payload)) { throw new InvalidArgumentException('RESULT_OBJECT_REQUIRED'); }
        return json_encode(self::normalizeResult($payload), JSON_THROW_ON_ERROR | JSON_UNESCAPED_SLASHES);
    }
}
