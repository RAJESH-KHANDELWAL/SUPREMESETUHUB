<?php
/** Read-only PHP metadata contract for GLOBAL_SHARED_HOSTING_HOSTING_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class GlobalSharedHostingHostingStorageEcosystem
{
    public const ECOSYSTEM_ID = 'GLOBAL_SHARED_HOSTING_HOSTING_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'SHARED_HOSTING';
    public const CATEGORY_GROUP = 'HOSTING_PLATFORMS';

    /** @return array<string,mixed> */
    public function describe(): array
    {
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'provider' => 'GLOBAL_HOSTING',
            'category' => self::CATEGORY,
            'category_group' => self::CATEGORY_GROUP,
            'connection_state' => 'NOT_CONFIGURED',
            'provider_product_verified' => false,
            'storage_operations_enabled' => false,
        ];
    }
}
