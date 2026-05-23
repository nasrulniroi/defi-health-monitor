CREATE TABLE IF NOT EXISTS tvl_history (
    id SERIAL PRIMARY KEY,
    protocol_slug VARCHAR(255) NOT NULL,
    tvl DECIMAL(20, 2) NOT NULL,
    timestamp BIGINT NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_tvl_history_slug ON tvl_history(protocol_slug);
