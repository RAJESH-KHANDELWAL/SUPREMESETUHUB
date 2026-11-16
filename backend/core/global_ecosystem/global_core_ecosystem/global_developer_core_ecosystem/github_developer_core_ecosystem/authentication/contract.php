<?php
/** Authenticated application context contract for github_developer Core. No credential material is accepted. */

declare(strict_types=1);

final class DeveloperGithubDeveloperAuthContextContract
{
    public const PROVIDER_ID = 'github_developer';
    public const ECOSYSTEM_ID = 'GLOBAL-DEVELOPER-GITHUB-DEVELOPER-CORE-ECOSYSTEM';

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
