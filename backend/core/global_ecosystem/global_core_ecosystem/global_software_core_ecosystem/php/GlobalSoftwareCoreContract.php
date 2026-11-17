<?php

declare(strict_types=1);

namespace SupremeSetuHub\GlobalSoftwareCore;

final class GlobalSoftwareCoreContract
{
    public const ECOSYSTEM_ID = 'GLOBAL-SOFTWARE-CORE-ECOSYSTEM';
    public const STATUS = 'CORE_CATALOG_ONLY';
    public const LIVE_CONNECTION_VERIFIED = false;
    public const EXECUTION_ENABLED = false;
    public const CREDENTIAL_STORAGE = 'EXTERNAL_SECRET_STORE_ONLY';

    /** @return array<string, mixed> */
    public static function manifest(): array
    {
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'status' => self::STATUS,
            'live_connection_verified' => self::LIVE_CONNECTION_VERIFIED,
            'execution_enabled' => self::EXECUTION_ENABLED,
            'credential_storage' => self::CREDENTIAL_STORAGE,
        ];
    }
}
