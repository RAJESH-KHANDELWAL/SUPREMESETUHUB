<?php
/** Read-only PHP metadata contract for GLOBAL_CLOUD_SMB_FILE_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class GlobalCloudSmbFileStorageEcosystem
{
    public const ECOSYSTEM_ID = 'GLOBAL_CLOUD_SMB_FILE_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'SMB_FILE_STORAGE';
    public const CATEGORY_GROUP = 'FILE_STORAGE';

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
