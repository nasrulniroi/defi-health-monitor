# DeFi Protocol Health Monitor

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-yellow.svg)](https://python.org)
[![Go 1.21+](https://img.shields.io/badge/Go-1.21+-cyan.svg)](https://go.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.4-blue.svg)](https://typescriptlang.org)
[![Tests](https://img.shields.io/badge/Tests-Passing-green.svg)](#testing)

Real-time risk intelligence platform for DeFi protocols across 8+ blockchains. Monitors TVL stability, APY sustainability, contract security, governance distribution, and liquidity depth to compute a composite **Protocol Health Score (PHS)**.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Dashboard (Next.js 14)                    │
│   ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐      │
│   │ Protocols│ │  Alerts  │ │ Analytics│ │  Risk    │      │
│   └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘      │
│        └────────────┼────────────┼────────────┘             │
│                     ▼            ▼                          │
│              ┌─────────────────────────┐                    │
│              │   FastAPI (Port 8000)   │                    │
│              └───────────┬─────────────┘                    │
│                          │                                  │
│   ┌──────────────────────┼──────────────────────┐          │
│   │                      ▼                      │          │
│   │              Risk Engine (Python)            │          │
│   │   ┌────────────┐ ┌────────────┐ ┌────────┐  │          │
│   │   │ TVL        │ │ APY        │ │Anomaly │  │          │
│   │   │ Analyzer   │ │ Calculator │ │Detector│  │          │
│   │   └────────────┘ └────────────┘ └────────┘  │          │
│   └─────────────────────────────────────────────┘          │
│                          │                                  │
│   ┌──────────────────────┼──────────────────────┐          │
│   │              Go Scanner (Port 8081)          │          │
│   │   ┌────────┐ ┌────────┐ ┌────────┐          │          │
│   │   │Ethereum│ │Arbitrum│ │Polygon │ ...      │          │
│   │   └────────┘ └────────┘ └────────┘          │          │
│   └─────────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────────┘
         │                │                │
         ▼                ▼                ▼
   DeFiLlama API    CoinGecko API    RPC Endpoints
```

## Risk Scoring Formula

The **Protocol Health Score (PHS)** is computed as:

```
PHS = 100 × (w₁·TVL_Stability + w₂·APY_Sustainability + w₃·Contract_Security + w₄·Governance_Distribution + w₅·Liquidity_Depth)
```

| Component | Weight | Description |
|-----------|--------|-------------|
| TVL Stability | w₁ = 0.30 | Coefficient of variation of 30-day TVL |
| APY Sustainability | w₂ = 0.20 | Deviation from 30-day average APY |
| Contract Security | w₃ = 0.25 | Number and quality of audits |
| Governance Distribution | w₄ = 0.15 | Decentralization of governance tokens |
| Liquidity Depth | w₅ = 0.10 | Daily volume to TVL ratio |

### Risk Levels

| Score | Level | Description |
|-------|-------|-------------|
| 75-100 | 🟢 Low | Healthy protocol, low risk |
| 50-74 | 🟡 Medium | Moderate risk, monitor closely |
| 25-49 | 🟠 High | Elevated risk, exercise caution |
| 0-24 | 🔴 Critical | High risk, potential issues |

## Screenshots

![Dashboard](docs/screenshots/dashboard.png)

![Protocol Explorer](docs/screenshots/protocols.png)

![Analytics](docs/screenshots/analytics.png)

![Alerts](docs/screenshots/alerts.png)

## Supported Chains

| Chain | Scanner | TVL Tracking | APY Monitoring |
|-------|---------|-------------|----------------|
| Ethereum | ✅ | ✅ | ✅ |
| Arbitrum | ✅ | ✅ | ✅ |
| Polygon | ✅ | ✅ | ✅ |
| BSC | ✅ | ✅ | ✅ |
| Avalanche | ✅ | ✅ | ✅ |
| Optimism | ✅ | ✅ | ✅ |
| Fantom | — | ✅ | ✅ |
| Solana | — | ✅ | ✅ |

## Quick Start

### Prerequisites

- Python 3.11+
- Go 1.21+
- Node.js 18+
- PostgreSQL 15+ (optional)

### Local Development

```bash
# Clone the repository
git clone https://github.com/nasrulniroi/defi-health-monitor.git
cd defi-health-monitor

# Install dependencies
make setup

# Start risk engine (Terminal 1)
cd src/engine && python main.py

# Start scanner (Terminal 2)
cd src/scanner && go run main.go serve

# Start frontend (Terminal 3)
cd src/web && npm run dev
```

### Docker

```bash
docker-compose up -d
```

## API Documentation

### Risk Engine (Port 8000)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/protocols` | GET | Health scores for top protocols |
| `/api/protocols/{id}` | GET | Detailed risk data for a protocol |
| `/api/risk/overview` | GET | Risk distribution overview |
| `/api/alerts` | GET | Active risk alerts |
| `/health` | GET | Health check |

### Scanner API (Port 8081)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/scan/results` | GET | Latest blockchain scan results |
| `/health` | GET | Health check |

## Testing

```bash
# All tests
make test

# Python tests
python -m pytest tests/engine/ tests/integration/ -v

# Go tests
cd src/scanner && go test -v ./...

# Frontend tests
cd src/web && npx vitest run
```

## Project Structure

```
defi-health-monitor/
├── src/
│   ├── engine/          # Python risk engine (FastAPI)
│   │   ├── risk_scorer.py      # PHS calculation
│   │   ├── tvl_analyzer.py     # TVL stability analysis
│   │   ├── apy_calculator.py   # APY sustainability
│   │   ├── anomaly_detector.py # Statistical anomaly detection
│   │   └── data/               # API clients (DeFiLlama, CoinGecko)
│   ├── scanner/         # Go blockchain scanner
│   │   └── internal/
│   │       ├── chain/          # Per-chain scanners
│   │       └── protocol/       # TVL/APY metrics
│   ├── web/             # Next.js dashboard
│   │   ├── app/                # Page routes
│   │   ├── components/         # React components
│   │   └── lib/                # Utilities
│   ├── db/              # Database schemas and migrations
│   └── scripts/         # Bash automation scripts
├── tests/               # Test suites
├── config/              # Configuration files
└── docs/                # Documentation
```

## Tech Stack

- **Frontend:** Next.js 14, TypeScript, Tailwind CSS, Recharts
- **Backend:** Python 3.11, FastAPI, NumPy, SciPy
- **Scanner:** Go 1.21, standard library
- **Database:** PostgreSQL (production), SQLite (development)
- **Data Sources:** DeFiLlama API, CoinGecko API, On-chain RPC
- **Infrastructure:** Docker, GitHub Actions CI/CD

## License

MIT License — see [LICENSE](LICENSE) for details.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
