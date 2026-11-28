<?php
declare(strict_types=1);
/** PHP interoperability facade; metadata only, no provider execution. */
final class GlobalIntegrationsCoreManager
{
    private const ID='GLOBAL-INTEGRATIONS-CORE-ECOSYSTEM';
    private const STATUS='CORE_CATALOG_ONLY';
    private const BLOCKED=['token','access_token','refresh_token','client_secret','api_key','secret','authorization','password','credential','private_key','webhook_secret','signing_secret','cookie','session','email','phone','mobile','address','date_of_birth','aadhaar_number','pan_number','bank_account','card_number','customer_payload','raw_payload'];
    public static function status(): array
    {
        return ['success'=>true,'ecosystem_id'=>self::ID,'status'=>self::STATUS,'provider_execution_enabled'=>false,'live_connection_verified'=>false];
    }
    public static function sanitizeMetadata(array $metadata): array
    {
        $safe=[];
        foreach($metadata as $key=>$value){
            if(in_array(strtolower((string)$key),self::BLOCKED,true)) continue;
            $safe[$key]=is_array($value)?self::sanitizeMetadata($value):$value;
        }
        return $safe;
    }
}
