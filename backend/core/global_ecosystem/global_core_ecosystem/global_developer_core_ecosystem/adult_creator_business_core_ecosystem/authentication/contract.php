<?php
/** Authenticated application context contract for adult_creator_business Core. No credential material is accepted. */

declare(strict_types=1);

final class DeveloperAdultCreatorBusinessAuthContextContract
{
    public const PROVIDER_ID = 'adult_creator_business';
    public const ECOSYSTEM_ID = 'GLOBAL-DEVELOPER-ADULT-CREATOR-BUSINESS-CORE-ECOSYSTEM';

    public static function validate(array $context): array
    {
        $required = ['tenant_id', 'actor_id', 'auth_context_id'];
        $missing = [];
        foreach ($required as $field) {
            if (!isset($context[$field]) || !is_string($context[$field]) || trim($context[$field]) === '') {
                $missing[] = $field;
            }
        }
        foreach (['password', 'secret', 'token', 'api_key', 'private_key', 'credential', 'authorization'] as $secretKey) {
            if (array_key_exists($secretKey, $context)) {
                return ['valid' => false, 'errors' => ['secret_material_not_allowed']];
            }
        }
        return ['valid' => $missing === [], 'errors' => $missing === [] ? [] : ['missing_context_fields'], 'missing' => $missing];
    }
}
