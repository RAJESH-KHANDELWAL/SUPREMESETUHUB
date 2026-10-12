<?php
declare(strict_types=1);

/** Checkout requires explicit country, tax and provider approval. */
final class GlobalMarketPolicy
{
    public function __construct(private readonly PDO $pdo) {}

    public function checkoutEligibility(string $countryCode, string $paymentMethodCode): array
    {
        $countryCode = strtoupper(trim($countryCode));
        $paymentMethodCode = strtoupper(trim($paymentMethodCode));
        if (!preg_match('/^[A-Z]{2}$/', $countryCode)) {
            return ['allowed' => false, 'reason' => 'INVALID_COUNTRY_CODE'];
        }
        if (!preg_match('/^[A-Z0-9_]{2,40}$/', $paymentMethodCode)) {
            return ['allowed' => false, 'reason' => 'INVALID_PAYMENT_METHOD'];
        }

        $sql = "SELECT c.country_code,c.country_name,c.default_currency,c.checkout_enabled,
                       c.payment_review_status,c.tax_review_status,p.method_code,
                       p.enabled AS payment_enabled,p.live_mode,p.activation_status,p.provider_account_verified
                FROM marketplace_countries c
                INNER JOIN marketplace_payment_methods p ON p.method_code = :method_code
                WHERE c.country_code = :country_code LIMIT 1";
        $statement = $this->pdo->prepare($sql);
        $statement->execute([':method_code' => $paymentMethodCode, ':country_code' => $countryCode]);
        $row = $statement->fetch();

        if (!$row) return ['allowed' => false, 'reason' => 'COUNTRY_OR_PAYMENT_METHOD_NOT_CONFIGURED'];
        if ((int) $row['checkout_enabled'] !== 1) return ['allowed' => false, 'reason' => 'COUNTRY_CHECKOUT_NOT_ENABLED'];
        if ($row['payment_review_status'] !== 'APPROVED') return ['allowed' => false, 'reason' => 'COUNTRY_PAYMENT_REVIEW_REQUIRED'];
        if ($row['tax_review_status'] !== 'VERIFIED') return ['allowed' => false, 'reason' => 'COUNTRY_TAX_REVIEW_REQUIRED'];
        if ((int) $row['payment_enabled'] !== 1 || (int) $row['live_mode'] !== 1) return ['allowed' => false, 'reason' => 'PAYMENT_METHOD_NOT_LIVE'];
        if ($row['activation_status'] !== 'APPROVED' || (int) $row['provider_account_verified'] !== 1) return ['allowed' => false, 'reason' => 'PAYMENT_PROVIDER_APPROVAL_REQUIRED'];

        return ['allowed' => true, 'country_code' => $row['country_code'],
            'country_name' => $row['country_name'], 'currency_code' => $row['default_currency'],
            'payment_method' => $row['method_code']];
    }
}
