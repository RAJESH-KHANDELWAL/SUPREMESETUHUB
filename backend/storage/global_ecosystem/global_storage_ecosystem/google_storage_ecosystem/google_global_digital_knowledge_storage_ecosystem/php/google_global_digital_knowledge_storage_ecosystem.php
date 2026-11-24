<?php
/** Read-only PHP metadata contract for GOOGLE_GLOBAL_DIGITAL_KNOWLEDGE_STORAGE_ECOSYSTEM. */
declare(strict_types=1);
final class GoogleGlobalDigitalKnowledgeStorageEcosystem
{
    public const ECOSYSTEM_ID = 'GOOGLE_GLOBAL_DIGITAL_KNOWLEDGE_STORAGE_ECOSYSTEM';
    public const CATEGORY = 'GLOBAL_DIGITAL_KNOWLEDGE';
    public const CATEGORY_GROUP = 'BHARAT_AND_GLOBAL';
    /** @return array<string,mixed> */
    public function describe(): array
    {
        return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GOOGLE','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];
    }
}
