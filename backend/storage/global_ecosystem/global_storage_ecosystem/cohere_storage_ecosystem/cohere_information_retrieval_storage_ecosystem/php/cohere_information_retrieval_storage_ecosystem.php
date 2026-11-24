<?php
/** Read-only PHP metadata contract for COHERE_INFORMATION_RETRIEVAL_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class CohereInformationRetrievalStorageEcosystem
{
    public const ECOSYSTEM_ID = 'COHERE_INFORMATION_RETRIEVAL_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'INFORMATION_RETRIEVAL';
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
