<?php
declare(strict_types=1);

/** Cohere Embed caller-context contract; credentials remain opaque references. */
final class CohereEmbedAuthenticationContext
{
    public const PROVIDER = 'cohere';
    public const CAPABILITY = 'embed';
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
