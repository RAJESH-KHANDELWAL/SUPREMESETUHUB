-- SUPREMESETUHUB: one physical database, one main identity and four logical gates.
-- Run only against the SUPREMESETUHUB database after taking a backup.
-- This migration does not touch either existing WordPress database.

CREATE TABLE IF NOT EXISTS ss_identity_gates (
    identity_code VARCHAR(80) NOT NULL,
    display_name VARCHAR(160) NOT NULL,
    gate_type VARCHAR(32) NOT NULL,
    storage_database VARCHAR(128) NOT NULL DEFAULT 'SUPREMESETUHUB',
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (identity_code),
    KEY idx_ss_identity_gates_active (is_active, gate_type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO ss_identity_gates
    (identity_code, display_name, gate_type, storage_database, is_active)
VALUES
    ('SUPREMESETUHUB', 'SUPREMESETUHUB Main', 'MAIN', 'SUPREMESETUHUB', 1),
    ('RAJESHKHANDELWALOFFICIAL', 'RAJESHKHANDELWALOFFICIAL', 'IDENTITY_GATE', 'SUPREMESETUHUB', 1),
    ('RAJESHKHANDELWAL', 'RAJESHKHANDELWAL', 'IDENTITY_GATE', 'SUPREMESETUHUB', 1),
    ('DRRAJESHKHANDELWALIBCOFFICIAL', 'DRRAJESHKHANDELWALIBCOFFICIAL', 'IDENTITY_GATE', 'SUPREMESETUHUB', 1),
    ('DRRAJESHKHANDELWALIBC', 'DRRAJESHKHANDELWALIBC', 'IDENTITY_GATE', 'SUPREMESETUHUB', 1)
ON DUPLICATE KEY UPDATE
    display_name = VALUES(display_name),
    gate_type = VALUES(gate_type),
    storage_database = VALUES(storage_database),
    is_active = VALUES(is_active);
