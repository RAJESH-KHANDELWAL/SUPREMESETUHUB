<?php
declare(strict_types=1);
final class ProductAuthenticationContract {
 public const PRODUCT_ID='google_appsheet';
 public const LIVE_CONNECTION_ENABLED=false;
 public static function validContext(array $c):bool{return isset($c['tenant_id'],$c['actor_id'])&&is_string($c['tenant_id'])&&is_string($c['actor_id'])&&$c['tenant_id']!==''&&$c['actor_id']!=='';}
}
