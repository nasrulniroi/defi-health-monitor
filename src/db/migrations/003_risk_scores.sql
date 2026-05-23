CREATE TABLE IF NOT EXISTS risk_scores (
    id SERIAL PRIMARY KEY,
    protocol_slug VARCHAR(255) NOT NULL,
    health_score DECIMAL(5, 2) NOT NULL,
    tvl_stability DECIMAL(5, 4),
    apy_sustainability DECIMAL(5, 4),
    contract_security DECIMAL(5, 4),
    governance_distribution DECIMAL(5, 4),
    liquidity_depth DECIMAL(5, 4),
    computed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_risk_scores_slug ON risk_scores(protocol_slug);
