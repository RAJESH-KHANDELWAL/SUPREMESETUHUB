<?php
declare(strict_types=1);
/** Read-only PHP metadata contract for GLOBAL_AI_EMBEDDINGS_AND_VECTORS_STORAGE_ECOSYSTEM. */
final class GlobalAIEmbeddingsAndVectorsStorageEcosystem {
 public const ECOSYSTEM_ID='GLOBAL_AI_EMBEDDINGS_AND_VECTORS_STORAGE_ECOSYSTEM';
 public const CATEGORY='EMBEDDINGS_AND_VECTORS';
 public const CATEGORY_GROUP='AI_PROMPT_AND_KNOWLEDGE';
 public function describe():array{return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GLOBAL_AI','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];}
}
