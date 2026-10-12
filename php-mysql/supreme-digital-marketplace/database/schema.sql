-- SUPREME DIGITAL DESIGN MARKETPLACE
-- MySQL 8.0+ / InnoDB / utf8mb4
-- Digital-only: no physical inventory, printing, packing, or shipping tables.

CREATE TABLE IF NOT EXISTS digital_designs (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    slug VARCHAR(180) NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(80) NOT NULL,
    preview_path VARCHAR(500) NOT NULL,
    private_storage_key VARCHAR(1000) NOT NULL,
    license_label VARCHAR(120) NOT NULL DEFAULT 'Personal digital use',
    status ENUM('DRAFT', 'IN_REVIEW', 'PUBLISHED', 'ARCHIVED') NOT NULL DEFAULT 'DRAFT',
    created_by VARCHAR(191) NOT NULL,
    published_at DATETIME NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_digital_designs_slug (slug),
    KEY idx_digital_designs_status_published (status, published_at),
    KEY idx_digital_designs_category_status (category, status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS digital_design_prices (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    design_id BIGINT UNSIGNED NOT NULL,
    market_code ENUM('IN', 'GLOBAL') NOT NULL,
    currency_code CHAR(3) NOT NULL,
    price_minor BIGINT UNSIGNED NOT NULL,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    valid_from DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_design_market_price (design_id, market_code),
    KEY idx_market_active_price (market_code, is_active),
    CONSTRAINT fk_digital_price_design FOREIGN KEY (design_id)
        REFERENCES digital_designs(id) ON DELETE CASCADE,
    CONSTRAINT chk_digital_price_currency CHECK (
        (market_code = 'IN' AND currency_code = 'INR') OR
        (market_code = 'GLOBAL' AND currency_code = 'USD')
    ),
    CONSTRAINT chk_digital_price_positive CHECK (price_minor > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS design_trend_signals (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    region_code VARCHAR(16) NOT NULL,
    topic VARCHAR(180) NOT NULL,
    source_name VARCHAR(120) NOT NULL,
    source_url VARCHAR(1000) NULL,
    signal_score DECIMAL(5,2) NOT NULL DEFAULT 0,
    evidence_count INT UNSIGNED NOT NULL DEFAULT 0,
    observed_at DATETIME NOT NULL,
    expires_at DATETIME NULL,
    review_status ENUM('UNREVIEWED', 'APPROVED', 'REJECTED', 'EXPIRED') NOT NULL DEFAULT 'UNREVIEWED',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_trend_region_freshness (region_code, observed_at),
    KEY idx_trend_review_score (review_status, signal_score)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS digital_orders (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    order_number VARCHAR(40) NOT NULL,
    customer_id VARCHAR(191) NOT NULL,
    customer_email VARCHAR(254) NOT NULL,
    market_code ENUM('IN', 'GLOBAL') NOT NULL,
    currency_code CHAR(3) NOT NULL,
    subtotal_minor BIGINT UNSIGNED NOT NULL,
    tax_minor BIGINT UNSIGNED NOT NULL DEFAULT 0,
    total_minor BIGINT UNSIGNED NOT NULL,
    payment_provider VARCHAR(80) NULL,
    provider_payment_id VARCHAR(191) NULL,
    payment_status ENUM('PENDING', 'PAID', 'FAILED', 'REFUNDED') NOT NULL DEFAULT 'PENDING',
    order_status ENUM('PENDING_PAYMENT', 'PAID', 'FULFILLED', 'CANCELLED', 'REFUNDED') NOT NULL DEFAULT 'PENDING_PAYMENT',
    paid_at DATETIME NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_digital_order_number (order_number),
    UNIQUE KEY uq_payment_provider_ref (payment_provider, provider_payment_id),
    KEY idx_customer_orders (customer_id, created_at),
    KEY idx_order_payment_status (payment_status, order_status),
    CONSTRAINT chk_digital_order_currency CHECK (
        (market_code = 'IN' AND currency_code = 'INR') OR
        (market_code = 'GLOBAL' AND currency_code = 'USD')
    )
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS digital_order_items (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    order_id BIGINT UNSIGNED NOT NULL,
    design_id BIGINT UNSIGNED NOT NULL,
    title_snapshot VARCHAR(200) NOT NULL,
    license_snapshot VARCHAR(120) NOT NULL,
    unit_price_minor BIGINT UNSIGNED NOT NULL,
    quantity SMALLINT UNSIGNED NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_order_design (order_id, design_id),
    CONSTRAINT fk_digital_item_order FOREIGN KEY (order_id)
        REFERENCES digital_orders(id) ON DELETE CASCADE,
    CONSTRAINT fk_digital_item_design FOREIGN KEY (design_id)
        REFERENCES digital_designs(id) ON DELETE RESTRICT,
    CONSTRAINT chk_digital_item_quantity CHECK (quantity = 1)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS digital_download_grants (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    order_item_id BIGINT UNSIGNED NOT NULL,
    token_hash CHAR(64) NOT NULL,
    expires_at DATETIME NOT NULL,
    max_downloads SMALLINT UNSIGNED NOT NULL DEFAULT 5,
    download_count SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    revoked_at DATETIME NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_download_token_hash (token_hash),
    KEY idx_download_expiry (expires_at, revoked_at),
    CONSTRAINT fk_download_order_item FOREIGN KEY (order_item_id)
        REFERENCES digital_order_items(id) ON DELETE CASCADE,
    CONSTRAINT chk_download_count CHECK (download_count <= max_downloads)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
