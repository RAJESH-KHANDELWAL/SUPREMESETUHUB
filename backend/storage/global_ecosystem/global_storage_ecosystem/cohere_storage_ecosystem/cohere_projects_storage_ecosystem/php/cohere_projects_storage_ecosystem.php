<?php
/** Read-only PHP metadata contract for COHERE_PROJECTS_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class CohereProjectsStorageEcosystem
{
    public const ECOSYSTEM_ID = 'COHERE_PROJECTS_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'PROJECTS';
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
