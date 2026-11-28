<?php
declare(strict_types=1);
final class GlobalSoftwareCoreContract
{
    public static function fromArray(array $payload): array
    {
        foreach (['token','access_token','refresh_token','client_secret','api_key','password'] as $key) { unset($payload[$key]); }
        $payload['live_connection_verified'] = false;
        $payload['api_calls_performed'] = 0;
        return $payload;
    }
}
