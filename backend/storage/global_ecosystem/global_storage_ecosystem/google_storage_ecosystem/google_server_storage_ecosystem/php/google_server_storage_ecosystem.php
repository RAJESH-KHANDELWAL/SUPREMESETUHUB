<?php
/** Read-only PHP metadata contract for GOOGLE_SERVER_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class GoogleServerStorageEcosystem
{
    public const ECOSYSTEM_ID = 'GOOGLE_SERVER_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'SERVER';
    public const CATEGORY_GROUP = 'DEVELOPER_AND_INFRASTRUCTURE';

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
