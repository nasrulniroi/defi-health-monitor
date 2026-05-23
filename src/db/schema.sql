CREATE TABLE IF NOT EXISTS protocols (
    id SERIAL PRIMARY KEY,
    slug VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    chain VARCHAR(100),
    category VARCHAR(100),
    tvl DECIMAL(20, 2) DEFAULT 0,
    apy DECIMAL(10, 4) DEFAULT 0,
    health_score DECIMAL(5, 2) DEFAULT 0,
    risk_level VARCHAR(20) DEFAULT 'unknown',
    audits INT DEFAULT 0,
    url TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tvl_history (
    id SERIAL PRIMARY KEY,
    protocol_slug VARCHAR(255) NOT NULL,
    tvl DECIMAL(20, 2) NOT NULL,
    timestamp BIGINT NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS risk_scores (
    id SERIAL PRIMARY KEY,
    protocol_slug VARCHAR(255) NOT NULL,
    health_score DECIMAL(5, 2) NOT NULL,
    tvl_stability DECIMAL(5, 4),
    apy_sustainability DECIMAL(5, 4),
    contract_security DECIMAL(5, 4),
    governance_distribution DECIMAL(5, 4),
    liquidity_depth DECIMAL(5, 4),
    risk_factors TEXT[],
    computed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS alerts (
    id SERIAL PRIMARY KEY,
    protocol_slug VARCHAR(255) NOT NULL,
    severity VARCHAR(20) NOT NULL,
    message TEXT NOT NULL,
    score DECIMAL(5, 2),
    factor VARCHAR(100),
    resolved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tvl_history_slug ON tvl_history(protocol_slug);
CREATE INDEX idx_risk_scores_slug ON risk_scores(protocol_slug);
CREATE INDEX idx_alerts_severity ON alerts(severity);
CREATE INDEX idx_alerts_resolved ON alerts(resolved);
