<?php
declare(strict_types=1);
final class AnthropicProductAuthenticationContract {
 public const PRODUCT_ID='anthropic_batches';
 public const LIVE_CONNECTION_ENABLED=false;
 public static function validContext(array $context): bool {
  return isset($context['tenant_id'],$context['actor_id'])
   && is_string($context['tenant_id']) && $context['tenant_id'] !== ''
   && is_string($context['actor_id']) && $context['actor_id'] !== '';
 }
}
