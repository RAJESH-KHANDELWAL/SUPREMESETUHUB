<?php
declare(strict_types=1);

/** DeepSeek chat_completions caller context contract. Credential values stay outside CORE. */
final class DeepSeekChatCompletionsAuthenticationContext
{
    public const PROVIDER = 'deepseek';
    public const CAPABILITY = 'chat_completions';
    public const LIVE_CONNECTION_ENABLED = false;

    public function __construct(
        public readonly string $tenantId,
        public readonly string $actorId,
        public readonly string $credentialReference
    ) {}

    public static function validContext(array $context): bool
    {
        return isset($context['tenant_id'], $context['actor_id'])
            && is_string($context['tenant_id'])
            && is_string($context['actor_id'])
            && trim($context['tenant_id']) !== ''
            && trim($context['actor_id']) !== '';
    }
}
