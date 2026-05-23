# Architecture

## System Overview

The DeFi Protocol Health Monitor consists of three main components:

### 1. Risk Engine (Python)
- Fetches protocol data from DeFiLlama and CoinGecko APIs
- Calculates Protocol Health Score (PHS) using weighted formula
- Detects anomalies in TVL and APY data
- Serves risk data via FastAPI

### 2. Blockchain Scanner (Go)
- High-performance on-chain data collection
- Supports 8+ EVM-compatible chains
- Reads block data, contract interactions, governance state
- Serves scan results via HTTP API

### 3. Dashboard (Next.js)
- Real-time protocol monitoring
- Interactive risk visualization
- Alert management
- Export and reporting

## Data Flow

```
DeFiLlama API ──┐
                ├──> Risk Engine ──> FastAPI ──> Dashboard
CoinGecko API ──┘        │
                         ▼
                   PostgreSQL
                         ▲
                         │
RPC Endpoints ──> Go Scanner ──> HTTP API
```

## Risk Scoring Formula

```
PHS = 100 × (w₁·TVL_Stability + w₂·APY_Sustainability + w₃·Contract_Security + w₄·Governance_Distribution + w₅·Liquidity_Depth)
```

See [RISK_MODEL.md](RISK_MODEL.md) for detailed explanation.
