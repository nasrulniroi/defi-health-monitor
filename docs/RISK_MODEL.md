# Risk Model Documentation

## Protocol Health Score (PHS)

The Protocol Health Score is a composite metric that evaluates the overall health and risk profile of a DeFi protocol.

## Formula

```
PHS = 100 × (w₁·TVL_Stability + w₂·APY_Sustainability + w₃·Contract_Security + w₄·Governance_Distribution + w₅·Liquidity_Depth)
```

## Components

### TVL Stability (w₁ = 0.30)
Measures how stable a protocol's Total Value Locked is over 30 days.
- Calculated as: 1 - (σ/μ) where σ is standard deviation and μ is mean of 30-day TVL
- Penalizes high volatility
- Considers trend direction (growing vs declining)

### APY Sustainability (w₂ = 0.20)
Evaluates whether current APY levels are sustainable.
- Compares current APY to 30-day average
- Heavily penalizes APY > 1000% (likely unsustainable)
- Considers 7-day volatility

### Contract Security (w₃ = 0.25)
Assesses smart contract security posture.
- Based on number of audits (0-3+)
- Higher weight for lending and bridge protocols
- Audit recency and auditor reputation

### Governance Distribution (w₄ = 0.15)
Measures how decentralized protocol governance is.
- Gini coefficient of governance token distribution
- Presence of treasury and governance mechanisms

### Liquidity Depth (w₅ = 0.10)
Evaluates the ratio of trading volume to TVL.
- Higher volume/TVL ratio indicates better liquidity
- Important for exit liquidity in stress events

## Risk Levels

| Score Range | Risk Level | Description |
|-------------|------------|-------------|
| 75-100      | Low        | Healthy protocol, low risk |
| 50-74       | Medium     | Moderate risk, monitor closely |
| 25-49       | High       | Elevated risk, exercise caution |
| 0-24        | Critical   | High risk, potential issues detected |

## Anomaly Detection

Statistical anomalies are detected using Z-score analysis:
- Z-score > 2.5 triggers anomaly flag
- Rapid TVL changes (>20% in 24h) flagged separately
- Whale withdrawal detection (>10% TVL drop in single period)
