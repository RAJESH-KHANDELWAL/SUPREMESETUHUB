<?php
/** Read-only PHP metadata contract for GLOBAL_INDIVIDUAL_PERSONAL_DEVICE_SYNCHRONIZATION_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class GlobalindividualpersonalDeviceSynchronizationstorageecosystem
{
    public const ECOSYSTEM_ID = 'GLOBAL_INDIVIDUAL_PERSONAL_DEVICE_SYNCHRONIZATION_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'PERSONAL_DEVICE_SYNCHRONIZATION';
    public const CATEGORY_GROUP = 'DEVICE_AND_CLOUD';

    /** @return array<string,mixed> */
    public function describe(): array
    {
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'provider' => 'GLOBAL_INDIVIDUAL',
            'category' => self::CATEGORY,
            'category_group' => self::CATEGORY_GROUP,
            'connection_state' => 'NOT_CONFIGURED',
            'provider_product_verified' => false,
            'storage_operations_enabled' => false,
        ];
    }
}
