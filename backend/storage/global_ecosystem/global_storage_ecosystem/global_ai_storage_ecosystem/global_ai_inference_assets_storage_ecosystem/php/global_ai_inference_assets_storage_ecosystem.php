<?php
declare(strict_types=1);
/** Read-only PHP metadata contract for GLOBAL_AI_INFERENCE_ASSETS_STORAGE_ECOSYSTEM. */
final class GlobalAIInferenceAssetsStorageEcosystem {
 public const ECOSYSTEM_ID='GLOBAL_AI_INFERENCE_ASSETS_STORAGE_ECOSYSTEM';
 public const CATEGORY='INFERENCE_ASSETS';
 public const CATEGORY_GROUP='AI_RUNTIME_AND_ORCHESTRATION';
 public function describe():array{return ['ecosystem_id'=>self::ECOSYSTEM_ID,'provider'=>'GLOBAL_AI','category'=>self::CATEGORY,'category_group'=>self::CATEGORY_GROUP,'connection_state'=>'NOT_CONFIGURED','provider_product_verified'=>false,'storage_operations_enabled'=>false];}
}
