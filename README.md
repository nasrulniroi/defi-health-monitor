# DeFi Protocol Health Monitor

> Real-time risk intelligence platform for DeFi protocols — monitors 50+ protocols across 12+ blockchain networks, computes composite health scores using a weighted multi-factor model, and surfaces critical risk alerts.

## Overview

DeFi Protocol Health Monitor is a full-stack system that continuously fetches on-chain data from DeFiLlama, CoinGecko, and other public APIs, then computes a **Protocol Health Score (PHS)** for each protocol using a formal composite risk formula. The system detects anomalies, tracks TVL migrations, monitors APY deviations, and alerts on critical risk events.

### What It Does

- **Monitors 50+ DeFi protocols** with TVL > $1M across Ethereum, Arbitrum, BSC, Polygon, Avalanche, Optimism, Fantom, Solana, Base, Tron, Bitcoin, Sui, and more
- **Computes Protocol Health Score (PHS)** using a 5-factor weighted model covering TVL stability, APY sustainability, security posture, governance maturity, and liquidity depth
- **Detects anomalies** — sudden TVL drops, APY spikes, governance attacks, liquidity drains
- **Real-time dashboard** with live data from DeFiLlama API, auto-refreshing every 5 minutes
- **Risk classification** — Low / Medium / High / Critical with color-coded visual indicators
- **Chain-level breakdown** — TVL distribution across all supported chains with visual charts
- **Alert system** — critical risk protocols highlighted with banner notifications

## Architecture

The system is composed of three main components:

### 1. Python Risk Engine (`src/engine/`)

Core risk scoring logic and data pipeline.

- `risk_scorer.py` — Composite PHS calculation using weighted multi-factor model
- `tvl_analyzer.py` — TVL trend analysis, anomaly detection, migration tracking
- `apy_calculator.py` — APY sustainability scoring, deviation alerts
- `anomaly_detector.py` — Statistical anomaly detection (Z-score, IQR, rolling window)
- `data/defillama.py` — DeFiLlama API client with caching
- `data/coingecko.py` — CoinGecko market data client
- `data/cache.py` — Redis-backed caching layer
- `protocol_registry.py` — Protocol metadata and categorization
- `utils/config.py` — YAML-based configuration management

### 2. Go Blockchain Scanner (`src/scanner/`)

High-performance concurrent blockchain scanner for on-chain data.

- `cmd/scan.go` — Main scan command with concurrent chain processing
- `cmd/serve.go` — HTTP API server for scanner results
- `internal/chain/` — Per-chain scanner implementations
- `internal/protocol/` — Protocol-specific data extraction
- `internal/rpc/client.go` — Multi-RPC client with failover

### 3. Next.js Frontend (`src/web/`)

Interactive dashboard with real-time visualization.

- `app/page.tsx` — Main dashboard layout
- `components/protocol-card.tsx` — Protocol summary cards
- `components/risk-gauge.tsx` — SVG risk gauge component
- `components/tvl-chart.tsx` — TVL distribution charts
- `components/alert-banner.tsx` — Critical alert notifications

### 4. Static Dashboard (`docs/`)

Deployed to GitHub Pages — a standalone HTML dashboard that fetches live data from DeFiLlama API and renders charts using Chart.js.

## Protocol Health Score (PHS) Formula

The composite risk score is calculated using a weighted multi-factor model:

```
PHS = Σ(wᵢ × Fᵢ) × 100

Where:
  F₁ = TVL Stability Score     (w₁ = 0.30)
  F₂ = APY Sustainability      (w₂ = 0.20)
  F₃ = Security Posture        (w₃ = 0.25)
  F₄ = Governance Maturity     (w₄ = 0.15)
  F₅ = Liquidity Depth         (w₅ = 0.10)

  Σwᵢ = 1.00
  PHS ∈ [0, 100]
```

### Factor Scoring

**F₁ — TVL Stability (0.30)**
| TVL Range | Score |
|-----------|-------|
| > $10B | 1.0 |
| > $1B | 0.8 |
| > $100M | 0.6 |
| > $10M | 0.4 |
| ≤ $10M | 0.2 |

**F₂ — APY Sustainability (0.20)**
| APY Range | Score | Rationale |
|-----------|-------|-----------|
| > 1000% | 0.1 | Unsustainable, likely Ponzi |
| > 200% | 0.3 | Very high risk |
| > 50% | 0.5 | Elevated risk |
| 0–50% | 0.8 | Normal range |
| N/A | 0.5 | Insufficient data |

**F₃ — Security Posture (0.25)**
| Audits | Score |
|--------|-------|
| ≥ 3 | 1.0 |
| ≥ 2 | 0.8 |
| ≥ 1 | 0.6 |
| 0 | 0.3 |

**F₄ — Governance Maturity (0.15)**
| Condition | Score |
|-----------|-------|
| Has governance ID | 0.7 |
| No governance | 0.3 |

**F₅ — Liquidity Depth (0.10)**
```
liqScore = min(1, (dailyVolume / TVL) × 2)
```

### Risk Classification

| PHS Range | Risk Level | Color |
|-----------|------------|-------|
| 75–100 | Low Risk | Green |
| 50–74 | Medium | Yellow |
| 25–49 | High Risk | Orange |
| 0–24 | Critical | Red |

## Data Sources

All data is fetched from public APIs with no authentication required:

| Source | Endpoint | Data |
|--------|----------|------|
| DeFiLlama | `/protocols` | Protocol TVL, category, chain, audits |
| DeFiLlama | `/v2/chains` | Per-chain TVL totals |
| DeFiLlama | `/overview/dexs` | DEX volumes 24h/7d/30d |
| DeFiLlama | `yields.llama.fi/pools` | Yield pools with APY, TVL |
| CoinGecko | `/coins/markets` | Market cap, price, volume |
| CoinGecko | `/search/trending` | Trending tokens |
| alternative.me | `/fng/` | Fear & Greed Index |
| Owlracle | `/v4/{chain}/gas` | Multi-chain gas prices |

## Supported Chains

Ethereum · Arbitrum · BSC · Polygon · Avalanche · Optimism · Fantom · Solana · Base · Tron · Bitcoin · Sui · zkSync · Linea · Scroll · Blast · Mantle · Gnosis · Celo

## Tech Stack

| Component | Language | Framework |
|-----------|----------|-----------|
| Risk Engine | Python 3.11+ | FastAPI, NumPy, Pandas |
| Blockchain Scanner | Go 1.21+ | Standard library, concurrent RPC |
| Frontend | TypeScript | Next.js, Tailwind CSS, shadcn/ui |
| Static Dashboard | HTML/CSS/JS | Chart.js, vanilla JS |
| Database | SQL | PostgreSQL 15+ |
| Cache | — | Redis 7+ |
| Containerization | Docker | Docker Compose |

## Project Structure

```
defi-health-monitor/
├── AGENTS.md                    # Agent development guide
├── CLAUDE.md                    # AI assistant instructions
├── CHANGELOG.md                 # Version history
├── CONTRIBUTING.md              # Contribution guidelines
├── LICENSE                      # MIT License
├── Makefile                     # Build automation
├── Dockerfile                   # Multi-stage container build
├── docker-compose.yml           # Service orchestration
├── package.json                 # Node.js dependencies
├── requirements.txt             # Python dependencies
├── config/
│   └── default.yaml             # Default configuration
├── docs/
│   └── index.html               # GitHub Pages dashboard
├── src/
│   ├── engine/                  # Python risk engine
│   │   ├── main.py
│   │   ├── risk_scorer.py
│   │   ├── tvl_analyzer.py
│   │   ├── apy_calculator.py
│   │   ├── anomaly_detector.py
│   │   ├── protocol_registry.py
│   │   ├── data/
│   │   │   ├── defillama.py
│   │   │   ├── coingecko.py
│   │   │   └── cache.py
│   │   └── utils/
│   │       └── config.py
│   ├── scanner/                 # Go blockchain scanner
│   │   ├── main.go
│   │   ├── go.mod
│   │   ├── cmd/
│   │   │   ├── scan.go
│   │   │   └── serve.go
│   │   └── internal/
│   │       ├── chain/
│   │       ├── protocol/
│   │       └── rpc/
│   └── web/                     # Next.js frontend
│       ├── package.json
│       ├── app/
│       │   ├── layout.tsx
│       │   └── page.tsx
│       └── components/
│           ├── protocol-card.tsx
│           ├── risk-gauge.tsx
│           ├── tvl-chart.tsx
│           └── alert-banner.tsx
└── tests/
    ├── engine/
    ├── scanner/
    └── integration/
```

## Quick Start

### Prerequisites

- Python 3.11+
- Go 1.21+
- Node.js 18+
- PostgreSQL 15+
- Redis 7+

### Installation

```bash
# Clone the repository
git clone https://github.com/nasrulniroi/defi-health-monitor.git
cd defi-health-monitor

# Install all dependencies
make setup

# Initialize database
make db-init

# Run all tests
make test

# Start all services
make run
```

### Docker

```bash
docker-compose up -d
```

### Static Dashboard

The static dashboard at `docs/index.html` is deployed to GitHub Pages and requires no backend — it fetches live data directly from DeFiLlama API.

## API Endpoints

### Risk Engine (Python/FastAPI)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/protocols` | All monitored protocols with PHS |
| GET | `/api/v1/protocols/{name}` | Single protocol detail |
| GET | `/api/v1/alerts` | Active critical alerts |
| GET | `/api/v1/chains` | Chain-level TVL breakdown |
| GET | `/api/v1/anomalies` | Detected anomalies |
| GET | `/api/v1/health` | Service health check |

### Scanner (Go)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/scan/{chain}` | Trigger chain scan |
| GET | `/api/v1/status` | Scanner status |

## Configuration

Configuration is managed via `config/default.yaml`:

```yaml
risk_engine:
  weights:
    tvl: 0.30
    apy: 0.20
    security: 0.25
    governance: 0.15
    liquidity: 0.10
  thresholds:
    critical: 25
    high: 50
    medium: 75

scanner:
  chains:
    - ethereum
    - arbitrum
    - bsc
    - polygon
  rpc_timeout: 10s
  concurrent_workers: 8

cache:
  ttl: 300  # seconds
  backend: redis
```

## Testing

```bash
# All tests
make test

# Python unit tests
cd src/engine && python -m pytest tests/engine/ -v

# Go tests
cd src/scanner && go test -v ./...

# Frontend tests
cd src/web && npx vitest run

# Coverage
make coverage
```

## Live Demo

**https://nasrulniroi.github.io/defi-health-monitor/**

The live dashboard fetches real-time data from DeFiLlama and displays:
- Total TVL across all monitored protocols
- Average health score with risk classification
- TVL distribution bar chart (top 20 protocols)
- Chain TVL doughnut chart
- Chain breakdown with horizontal bars
- Full protocol table with sortable columns
- Critical risk alert banner
- Search and filter functionality

## License

MIT License — see [LICENSE](LICENSE) for details.
