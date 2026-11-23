<?php
declare(strict_types=1);
/** Sanitized transport-neutral Stripe Core result contract. */
final class StripeCoreContract {
 private const BLOCKED=['token','access_token','refresh_token','client_secret','secret_key','api_key','authorization','pan','cvc','card_number'];
 private array $payload;
 private function __construct(array $payload){$this->payload=self::sanitize($payload);}
 public static function fromArray(array $payload):self{return new self($payload);}
 public static function fromJson(string $json):self{$data=json_decode($json,true,512,JSON_THROW_ON_ERROR);if(!is_array($data))throw new InvalidArgumentException('STRIPE_CORE_RESULT_MUST_BE_OBJECT');return new self($data);}
 private static function sanitize(array $data):array{$safe=[];foreach($data as $key=>$value){if(in_array(strtolower((string)$key),self::BLOCKED,true))continue;$safe[$key]=is_array($value)?self::sanitize($value):$value;}return $safe;}
 public function toArray():array{return $this->payload;}
 public function toJson():string{return json_encode($this->payload,JSON_THROW_ON_ERROR|JSON_UNESCAPED_SLASHES);}
 public function isLiveConnectionVerified():bool{return ($this->payload['live_connection_verified']??false)===true;}
}
