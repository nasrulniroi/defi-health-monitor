# Agent Development Guide

This document provides comprehensive guidance for AI agents working on the DeFi Protocol Health Monitor project.

## Development Environment Setup

### Required Tools

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.11+ | Risk engine, API server |
| Go | 1.21+ | Blockchain scanner |
| Node.js | 18+ | Frontend build |
| PostgreSQL | 15+ | Primary database |
| Redis | 7+ | Caching layer |
| Docker | 24+ | Containerization |
| Make | 3.8+ | Build automation |

### Quick Setup

```bash
make setup          # Install all dependencies
make db-init        # Initialize database
make test           # Run all tests
make run            # Start all services
```

## Project Structure

### Component Overview

The system has three main components:

1. **Python Risk Engine** (`src/engine/`) — Core risk scoring logic, data fetching from DeFiLlama and CoinGecko APIs, statistical analysis
2. **Go Scanner** (`src/scanner/`) — High-performance blockchain scanner that reads on-chain data from 8+ chains
3. **Next.js Frontend** (`src/web/`) — Dashboard UI with real-time charts and protocol explorer

### File Dependency Chain

```
config/default.yaml
    └──> src/engine/utils/config.py
         └──> src/engine/main.py
              ├──> src/engine/risk_scorer.py
              │    ├──> src/engine/tvl_analyzer.py
              │    ├──> src/engine/apy_calculator.py
              │    ├──> src/engine/anomaly_detector.py
              │    └──> src/engine/protocol_registry.py
              ├──> src/engine/data/defillama.py
              ├──> src/engine/data/coingecko.py
              └──> src/engine/data/cache.py

src/scanner/go.mod
    └──> src/scanner/main.go
         ├──> src/scanner/cmd/scan.go
         ├──> src/scanner/cmd/serve.go
         └──> src/scanner/internal/
              ├──> chain/*.go
              ├──> protocol/*.go
              └──> rpc/client.go

src/web/package.json
    └──> src/web/app/layout.tsx
         └──> src/web/app/page.tsx
              ├──> src/web/components/protocol-card.tsx
              ├──> src/web/components/risk-gauge.tsx
              ├──> src/web/components/tvl-chart.tsx
              └──> src/web/components/alert-banner.tsx
```

## Testing Commands

```bash
# All tests
make test

# Python unit tests
cd src/engine && python -m pytest tests/engine/ -v --tb=short

# Python integration tests
cd src/engine && python -m pytest tests/integration/ -v

# Go tests
cd src/scanner && go test -v ./...

# Frontend tests
cd src/web && npx vitest run

# Coverage reports
make coverage
```

## Deployment Guide

### Local Development

```bash
# Terminal 1: Risk engine
cd src/engine && python main.py

# Terminal 2: Scanner
cd src/scanner && go run main.go scan

# Terminal 3: Frontend
cd src/web && npm run dev
```

### Production with Docker

```bash
docker-compose -f docker-compose.yml up -d
```

### Manual Production Deployment

```bash
make build          # Build all binaries
make db-migrate     # Run database migrations
make deploy         # Deploy to production
```

## Code Conventions

### Python

- Use type hints on all function signatures
- Follow PEP 8 with 120 char line limit
- Use `dataclass` or `pydantic` for data models
- Docstrings in Google format
- All public functions must have docstrings

### Go

- Follow standard Go conventions (`gofmt`)
- Use table-driven tests
- Error handling: always check and wrap errors
- Use context for cancellation
- Package-level documentation required

### TypeScript

- Use strict TypeScript (`strict: true`)
- Functional components with hooks
- Tailwind CSS for styling
- shadcn/ui component library
- Prefer `const` assertions and template literals

### General

- No hardcoded secrets — use environment variables
- All API responses follow `{ data, error, timestamp }` format
- Log at appropriate levels (debug, info, warn, error)
- Write tests for all new features
- Update documentation when changing public APIs

## Adding a New Chain

1. Create `src/scanner/internal/chain/newchain.go`
2. Implement the `ChainScanner` interface
3. Add chain config to `config/chains.yaml`
4. Register in `src/scanner/cmd/scan.go`
5. Add tests in `tests/scanner/`
6. Update README chain support table

## Adding a New Risk Factor

1. Create analysis function in `src/engine/`
2. Add weight to `config/default.yaml`
3. Update `risk_scorer.py` composite calculation
4. Add to `protocol_registry.py` if needed
5. Update frontend display in `risk-gauge.tsx`
6. Update `docs/RISK_MODEL.md`
7. Add tests
