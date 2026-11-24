<?php
declare(strict_types=1);

/**
 * PHP interoperability facade for the Python-canonical finance business CORE.
 * This facade validates and normalizes metadata only; it never moves money,
 * connects to a financial provider, makes credit decisions or underwrites risk.
 */
require_once __DIR__ . '/php/FinanceServiceWorkBusinessContract.php';
require_once __DIR__ . '/php/FinanceServiceWorkBusinessDomainContract.php';

final class FinanceServiceWorkBusinessManager
{
    public const ECOSYSTEM_ID = 'GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM';
    public const CANONICAL_CORE_ID = 'GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-CORE-ECOSYSTEM';

    public static function normalizeResult(array $payload): array
    {
        return FinanceServiceWorkBusinessContract::fromArray($payload)->toArray();
    }

    public static function normalizeDomain(array $payload): array
    {
        return FinanceServiceWorkBusinessDomainContract::fromArray($payload)->toArray();
    }

    public static function executionEnabled(): bool
    {
        return false;
    }
}
