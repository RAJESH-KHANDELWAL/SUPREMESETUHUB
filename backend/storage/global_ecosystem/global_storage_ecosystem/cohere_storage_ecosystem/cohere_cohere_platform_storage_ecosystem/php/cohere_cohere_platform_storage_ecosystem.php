<?php
/** Read-only PHP metadata contract for COHERE_COHERE_PLATFORM_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class CohereCoherePlatformStorageEcosystem
{
    public const ECOSYSTEM_ID = 'COHERE_COHERE_PLATFORM_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'COHERE_PLATFORM';
    public const CATEGORY_GROUP = 'DEVELOPER_AND_PLATFORM';

    /** @return array<string,mixed> */
    public function describe(): array
    {
        return [
            'ecosystem_id' => self::ECOSYSTEM_ID,
            'provider' => 'COHERE',
            'category' => self::CATEGORY,
            'category_group' => self::CATEGORY_GROUP,
            'connection_state' => 'NOT_CONFIGURED',
            'provider_product_verified' => false,
            'storage_operations_enabled' => false,
        ];
    }
}
