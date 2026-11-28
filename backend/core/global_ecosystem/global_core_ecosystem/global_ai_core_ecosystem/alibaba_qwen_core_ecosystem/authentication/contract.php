<?php
declare(strict_types=1);
final class AlibabaQwenProductCoreServiceCallerContext {
 public const PROVIDER_ID='alibaba_qwen';
 public const LIVE_CONNECTION_VERIFIED=false;
 public static function isValid(array $c): bool{return isset($c['tenant_id'],$c['actor_id'])&&is_string($c['tenant_id'])&&trim($c['tenant_id'])!==''&&is_string($c['actor_id'])&&trim($c['actor_id'])!=='';}
}
