<?php
declare(strict_types=1);

/**
 * Read-only PHP 8+ normalizer for GLOBAL SERVER CORE scope metadata.
 * This class validates catalog shape; it does not authorize deployments.
 */
final class GlobalServerCoreScopeContract
{
    public static function normalize(array $payload): array
    {
        $tiers = $payload['service_tiers'] ?? [];
        $domains = $payload['workload_domains'] ?? [];
        $geography = $payload['geographic_scope'] ?? null;

        if (!is_array($tiers) || !is_array($domains) || !is_array($geography)) {
            throw new InvalidArgumentException('Invalid server scope catalog structure');
        }

        $requiredTiers = [
            'NORMAL', 'BASIC', 'STANDARD', 'PREMIUM',
            'PROFESSIONAL', 'ENTERPRISE', 'SUPREME',
        ];
        $actualTiers = [];
        foreach ($tiers as $tier) {
            if (!is_array($tier) || !isset($tier['tier_id'])) {
                throw new InvalidArgumentException('Each service tier requires tier_id');
            }
            $actualTiers[] = strtoupper((string) $tier['tier_id']);
        }
        if ($actualTiers !== $requiredTiers) {
            throw new InvalidArgumentException('Service tier order does not match the canonical contract');
        }

        foreach ($domains as $domain) {
            if (!is_array($domain) || empty($domain['domain_id'])) {
                throw new InvalidArgumentException('Each workload domain requires domain_id');
            }
        }

        return [
            'service_tiers' => $tiers,
            'workload_domains' => $domains,
            'geographic_scope' => $geography,
            'authorization_granted' => false,
            'remote_operations_enabled' => false,
        ];
    }
}
