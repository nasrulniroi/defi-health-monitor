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
CREATE INDEX idx_alerts_severity ON alerts(severity);
