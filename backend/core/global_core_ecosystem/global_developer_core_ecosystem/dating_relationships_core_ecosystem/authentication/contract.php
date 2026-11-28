<?php
/** Authenticated application context contract for dating_relationships Core. No credential material is accepted. */

declare(strict_types=1);

final class DeveloperDatingRelationshipsAuthContextContract
{
    public const PROVIDER_ID = 'dating_relationships';
    public const ECOSYSTEM_ID = 'GLOBAL-DEVELOPER-DATING-RELATIONSHIPS-CORE-ECOSYSTEM';

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
