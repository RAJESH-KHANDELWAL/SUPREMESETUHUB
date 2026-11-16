<?php
/** Read-only PHP metadata contract for COHERE_DOCUMENT_RETRIEVAL_STORAGE_ECOSYSTEM. */
declare(strict_types=1);

final class CohereDocumentRetrievalStorageEcosystem
{
    public const ECOSYSTEM_ID = 'COHERE_DOCUMENT_RETRIEVAL_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'DOCUMENT_RETRIEVAL';
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
