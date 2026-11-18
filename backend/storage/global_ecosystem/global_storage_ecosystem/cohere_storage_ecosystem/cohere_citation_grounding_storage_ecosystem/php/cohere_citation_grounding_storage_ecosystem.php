<?php
/** Read-only PHP metadata contract for COHERE_CITATION_GROUNDING_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class CohereCitationGroundingStorageEcosystem
{
    public const ECOSYSTEM_ID = 'COHERE_CITATION_GROUNDING_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'CITATION_GROUNDING';
    public const CATEGORY_GROUP = 'RETRIEVAL_AND_KNOWLEDGE';

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
