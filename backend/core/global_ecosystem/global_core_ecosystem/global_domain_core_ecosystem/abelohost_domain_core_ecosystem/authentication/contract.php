<?php
declare(strict_types=1);

namespace SupremeSetuHub\Core\Domain\Providers\Abelohost;

/** Shape-only auth-context contract. This does not authenticate or verify tokens. */
final class DomainAbelohostAuthContextContract
{
    public const PROVIDER_ID = 'abelohost';
    public const REQUIRED_FIELDS = ['tenant_id', 'authorization_context_id'];

    public static function hasRequiredShape(array $context): bool
    {
        foreach (self::REQUIRED_FIELDS as $field) {
            if (!isset($context[$field]) || !is_string($context[$field]) || trim($context[$field]) === '') {
                return false;
            }
        }
        return true;
    }
}
