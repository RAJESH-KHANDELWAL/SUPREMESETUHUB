-- Global digital sales configuration for SUPREME.
-- No tax rates are invented or automatically treated as verified.
-- Populate and verify country rules before setting checkout_enabled = 1.
-- Digital-only: no physical fulfillment/shipping tables are included.

CREATE TABLE IF NOT EXISTS marketplace_currencies (
 currency_code CHAR(3) NOT NULL, currency_name VARCHAR(100) NOT NULL,
 minor_unit TINYINT UNSIGNED NOT NULL DEFAULT 2, is_active TINYINT(1) NOT NULL DEFAULT 1,
 source_name VARCHAR(120) NULL, verified_at DATETIME NULL, PRIMARY KEY(currency_code),
 CONSTRAINT chk_currency_minor_unit CHECK(minor_unit <= 4)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS marketplace_countries (
 country_code CHAR(2) NOT NULL, country_name VARCHAR(120) NOT NULL, default_currency CHAR(3) NULL,
 storefront_enabled TINYINT(1) NOT NULL DEFAULT 1, checkout_enabled TINYINT(1) NOT NULL DEFAULT 0,
 payment_review_status ENUM('UNREVIEWED','REVIEW_REQUIRED','APPROVED','RESTRICTED') NOT NULL DEFAULT 'UNREVIEWED',
 tax_review_status ENUM('UNVERIFIED','REVIEW_REQUIRED','VERIFIED') NOT NULL DEFAULT 'UNVERIFIED',
 restriction_reason VARCHAR(500) NULL, reviewed_by VARCHAR(191) NULL, reviewed_at DATETIME NULL,
 updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY(country_code), KEY idx_country_storefront_checkout(storefront_enabled,checkout_enabled),
 CONSTRAINT fk_country_currency FOREIGN KEY(default_currency) REFERENCES marketplace_currencies(currency_code) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS marketplace_tax_rules (
 id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, country_code CHAR(2) NOT NULL, region_code VARCHAR(32) NOT NULL DEFAULT '',
 tax_name VARCHAR(120) NOT NULL, tax_type ENUM('VAT','GST','SALES_TAX','DIGITAL_SERVICES_TAX','OTHER') NOT NULL,
 rate_percent DECIMAL(7,4) NULL, calculation_mode ENUM('EXCLUSIVE','INCLUSIVE','REVERSE_CHARGE','NOT_APPLICABLE') NOT NULL DEFAULT 'EXCLUSIVE',
 applies_to_digital_goods TINYINT(1) NOT NULL DEFAULT 1, registration_required TINYINT(1) NOT NULL DEFAULT 1,
 registration_status ENUM('UNKNOWN','NOT_REGISTERED','REGISTERED','NOT_REQUIRED') NOT NULL DEFAULT 'UNKNOWN',
 effective_from DATE NULL, effective_to DATE NULL, source_url VARCHAR(1000) NULL,
 verification_status ENUM('UNVERIFIED','VERIFIED','EXPIRED','LEGAL_REVIEW_REQUIRED') NOT NULL DEFAULT 'UNVERIFIED',
 verified_by VARCHAR(191) NULL, verified_at DATETIME NULL, notes TEXT NULL,
 created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY(id), KEY idx_tax_country_region(country_code,region_code), KEY idx_tax_verification_effective(verification_status,effective_from,effective_to),
 CONSTRAINT fk_tax_country FOREIGN KEY(country_code) REFERENCES marketplace_countries(country_code) ON DELETE RESTRICT,
 CONSTRAINT chk_tax_rate_range CHECK(rate_percent IS NULL OR (rate_percent >= 0 AND rate_percent <= 100)),
 CONSTRAINT chk_tax_date_range CHECK(effective_to IS NULL OR effective_from IS NULL OR effective_to >= effective_from)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS marketplace_fx_rates (
 id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, base_currency CHAR(3) NOT NULL, quote_currency CHAR(3) NOT NULL,
 rate DECIMAL(24,10) NOT NULL, source_name VARCHAR(120) NOT NULL, observed_at DATETIME NOT NULL,
 expires_at DATETIME NOT NULL, status ENUM('UNVERIFIED','ACTIVE','EXPIRED') NOT NULL DEFAULT 'UNVERIFIED',
 PRIMARY KEY(id), UNIQUE KEY uq_fx_pair_observed(base_currency,quote_currency,observed_at),
 KEY idx_fx_pair_fresh(base_currency,quote_currency,status,expires_at),
 CONSTRAINT fk_fx_base FOREIGN KEY(base_currency) REFERENCES marketplace_currencies(currency_code) ON DELETE RESTRICT,
 CONSTRAINT fk_fx_quote FOREIGN KEY(quote_currency) REFERENCES marketplace_currencies(currency_code) ON DELETE RESTRICT,
 CONSTRAINT chk_fx_positive CHECK(rate > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS marketplace_payment_methods (
 id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, method_code VARCHAR(40) NOT NULL, provider_name VARCHAR(80) NOT NULL,
 display_name VARCHAR(100) NOT NULL, market_scope ENUM('IN','GLOBAL','BOTH') NOT NULL,
 enabled TINYINT(1) NOT NULL DEFAULT 0, live_mode TINYINT(1) NOT NULL DEFAULT 0,
 supported_currencies JSON NULL, supported_country_codes JSON NULL, required_env_keys JSON NOT NULL,
 activation_status ENUM('NOT_CONFIGURED','NEEDS_KYC','TESTING','APPROVED','SUSPENDED') NOT NULL DEFAULT 'NOT_CONFIGURED',
 provider_account_verified TINYINT(1) NOT NULL DEFAULT 0, last_verified_at DATETIME NULL,
 created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 PRIMARY KEY(id), UNIQUE KEY uq_payment_method_code(method_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS marketplace_campaign_calendar (
 id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, campaign_key VARCHAR(160) NOT NULL, title VARCHAR(200) NOT NULL,
 country_codes JSON NOT NULL, region_or_audience VARCHAR(160) NULL, starts_on DATE NOT NULL, ends_on DATE NOT NULL,
 source_name VARCHAR(120) NOT NULL, source_url VARCHAR(1000) NULL,
 status ENUM('IDEA','VERIFIED','ACTIVE','ENDED','REJECTED') NOT NULL DEFAULT 'IDEA',
 design_brief TEXT NULL, reviewed_at DATETIME NULL, created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY(id), UNIQUE KEY uq_campaign_key(campaign_key), KEY idx_campaign_dates_status(starts_on,ends_on,status),
 CONSTRAINT chk_campaign_date_range CHECK(ends_on >= starts_on)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO marketplace_currencies(currency_code,currency_name,minor_unit,source_name) VALUES
('INR','Indian Rupee',2,'ISO 4217'),('USD','US Dollar',2,'ISO 4217'),('EUR','Euro',2,'ISO 4217'),('GBP','Pound Sterling',2,'ISO 4217'),('CAD','Canadian Dollar',2,'ISO 4217'),('AUD','Australian Dollar',2,'ISO 4217'),('NZD','New Zealand Dollar',2,'ISO 4217'),('SGD','Singapore Dollar',2,'ISO 4217'),('AED','UAE Dirham',2,'ISO 4217'),('SAR','Saudi Riyal',2,'ISO 4217'),('QAR','Qatari Riyal',2,'ISO 4217'),('KWD','Kuwaiti Dinar',3,'ISO 4217'),('BHD','Bahraini Dinar',3,'ISO 4217'),('OMR','Omani Rial',3,'ISO 4217'),('JPY','Japanese Yen',0,'ISO 4217'),('CNY','Chinese Yuan Renminbi',2,'ISO 4217'),('HKD','Hong Kong Dollar',2,'ISO 4217'),('KRW','South Korean Won',0,'ISO 4217'),('THB','Thai Baht',2,'ISO 4217'),('MYR','Malaysian Ringgit',2,'ISO 4217'),('IDR','Indonesian Rupiah',2,'ISO 4217'),('PHP','Philippine Peso',2,'ISO 4217'),('VND','Vietnamese Dong',0,'ISO 4217'),('PKR','Pakistani Rupee',2,'ISO 4217'),('BDT','Bangladeshi Taka',2,'ISO 4217'),('LKR','Sri Lankan Rupee',2,'ISO 4217'),('NPR','Nepalese Rupee',2,'ISO 4217'),('ZAR','South African Rand',2,'ISO 4217'),('NGN','Nigerian Naira',2,'ISO 4217'),('KES','Kenyan Shilling',2,'ISO 4217'),('GHS','Ghanaian Cedi',2,'ISO 4217'),('EGP','Egyptian Pound',2,'ISO 4217'),('MAD','Moroccan Dirham',2,'ISO 4217'),('TRY','Turkish Lira',2,'ISO 4217'),('CHF','Swiss Franc',2,'ISO 4217'),('SEK','Swedish Krona',2,'ISO 4217'),('NOK','Norwegian Krone',2,'ISO 4217'),('DKK','Danish Krone',2,'ISO 4217'),('PLN','Polish Zloty',2,'ISO 4217'),('CZK','Czech Koruna',2,'ISO 4217'),('HUF','Hungarian Forint',2,'ISO 4217'),('RON','Romanian Leu',2,'ISO 4217'),('BRL','Brazilian Real',2,'ISO 4217'),('MXN','Mexican Peso',2,'ISO 4217'),('ARS','Argentine Peso',2,'ISO 4217'),('CLP','Chilean Peso',0,'ISO 4217'),('COP','Colombian Peso',2,'ISO 4217'),('PEN','Peruvian Sol',2,'ISO 4217'),('UAH','Ukrainian Hryvnia',2,'ISO 4217')
ON DUPLICATE KEY UPDATE currency_name=VALUES(currency_name),minor_unit=VALUES(minor_unit);

INSERT INTO marketplace_payment_methods(method_code,provider_name,display_name,market_scope,enabled,live_mode,supported_currencies,supported_country_codes,required_env_keys,activation_status) VALUES
('UPI_INDIA','UPI-compatible payment gateway','UPI','IN',0,0,JSON_ARRAY('INR'),JSON_ARRAY('IN'),JSON_ARRAY('SUPREME_UPI_PAYEE_VPA','SUPREME_PAYMENT_GATEWAY_KEY','SUPREME_PAYMENT_GATEWAY_SECRET'),'NOT_CONFIGURED'),
('PAYPAL_GLOBAL','PayPal','PayPal','GLOBAL',0,0,JSON_ARRAY('USD','EUR','GBP','CAD','AUD','SGD'),JSON_ARRAY(),JSON_ARRAY('SUPREME_PAYPAL_CLIENT_ID','SUPREME_PAYPAL_CLIENT_SECRET','SUPREME_PAYPAL_MERCHANT_EMAIL'),'NOT_CONFIGURED'),
('CARD_GLOBAL','Approved card payment gateway','Credit / Debit Card','BOTH',0,0,JSON_ARRAY('USD','EUR','GBP','INR'),JSON_ARRAY(),JSON_ARRAY('SUPREME_PAYMENT_GATEWAY_KEY','SUPREME_PAYMENT_GATEWAY_SECRET'),'NOT_CONFIGURED')
ON DUPLICATE KEY UPDATE display_name=VALUES(display_name),required_env_keys=VALUES(required_env_keys);
