<?php
/** Read-only PHP metadata contract for GLOBAL_CLOUD_CLOUD_NAS_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class GlobalCloudCloudNasStorageEcosystem
{
    public const ECOSYSTEM_ID = 'GLOBAL_CLOUD_CLOUD_NAS_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'CLOUD_NAS_STORAGE';
    public const CATEGORY_GROUP = 'HYBRID_MULTI_CLOUD_STORAGE';

    /** @return array<string,mixed> */
    public function describe(): array
    {
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'provider_scope' => 'GLOBAL_CLOUD_PROVIDER_NEUTRAL',
            'category' => self::CATEGORY,
            'category_group' => self::CATEGORY_GROUP,
            'connection_state' => 'NOT_CONFIGURED',
            'provider_product_verified' => false,
            'storage_operations_enabled' => false,
        ];
    }
}
