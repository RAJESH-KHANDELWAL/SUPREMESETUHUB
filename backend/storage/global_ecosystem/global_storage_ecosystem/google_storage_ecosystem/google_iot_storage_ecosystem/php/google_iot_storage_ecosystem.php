<?php
/** Read-only PHP metadata contract for GOOGLE_IOT_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class GoogleIotStorageEcosystem
{
    public const ECOSYSTEM_ID = 'GOOGLE_IOT_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'IOT';
    public const CATEGORY_GROUP = 'DEVICES_AND_OPERATING_SYSTEM';

    /** @return array<string,mixed> */
    public function describe(): array
    {
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'provider' => 'GOOGLE',
            'category' => self::CATEGORY,
            'category_group' => self::CATEGORY_GROUP,
            'connection_state' => 'NOT_CONFIGURED',
            'provider_product_verified' => false,
            'storage_operations_enabled' => false,
        ];
    }
}
