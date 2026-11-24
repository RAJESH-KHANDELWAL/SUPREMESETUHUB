<?php
declare(strict_types=1);
/** PHP 8+ metadata facade; no Hugging Face API calls or credential access. */
final class HuggingFaceCoreManager
{
    public const ECOSYSTEM_ID = 'HUGGINGFACE-CORE-ECOSYSTEM';
    public const ECOSYSTEM_NAME = 'HUGGING FACE CORE ECOSYSTEM';
    public function status(): array
    {
        return ['success'=>true,'ecosystem_id'=>self::ECOSYSTEM_ID,'name'=>self::ECOSYSTEM_NAME,
            'layer'=>'CORE','status'=>'CORE_CATALOG_ONLY','live_connection_verified'=>false,
            'connected'=>false,'api_calls_performed'=>0,'remote_operations_enabled'=>false,
            'credential_storage'=>'EXTERNAL_SECRET_STORE_ONLY'];
    }
    public function sanitize(array $payload): array
    {
        $blocked=['token','access_token','refresh_token','api_key','password','authorization','secret','private_key'];
        $safe=[];
        foreach($payload as $key=>$value){
            if(in_array(strtolower((string)$key),$blocked,true)) continue;
            $safe[$key]=is_array($value)?$this->sanitize($value):$value;
        }
        return $safe;
    }
}
