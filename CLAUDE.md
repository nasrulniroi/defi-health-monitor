# Claude Code Integration Guide

This document describes how to use Claude Code effectively with the DeFi Protocol Health Monitor project.

## Project Awareness

When starting a Claude Code session in this repository, Claude will automatically detect the project structure. This guide helps Claude understand the architecture and conventions.

## Common Commands

### Development

```bash
# Start full stack for development
make dev

# Run specific component
make dev-engine     # Python risk engine only
make dev-scanner    # Go scanner only
make dev-web        # Next.js frontend only
```

### Testing

```bash
# Run all tests with coverage
make test-coverage

# Run specific test suites
make test-engine    # Python tests
make test-scanner   # Go tests
make test-web       # Frontend tests
make test-integration  # Integration tests

# Watch mode for development
cd src/engine && pytest-watch
cd src/web && npm run test:watch
```

### Database

```bash
# Initialize database
make db-init

# Run migrations
make db-migrate

# Reset database (development only)
make db-reset

# Seed with protocol data
make db-seed
```

### Build and Deploy

```bash
# Build all binaries
make build

# Build Docker images
make docker-build

# Deploy to staging
make deploy-staging

# Deploy to production
make deploy-prod
```

## Testing Patterns

### Python Tests

```python
# Unit test pattern
import pytest
from engine.risk_scorer import RiskScorer

def test_risk_score_computation():
    scorer = RiskScorer()
    score = scorer.compute_phl(
        tvl_stability=0.85,
        apy_sustainability=0.90,
        contract_security=0.95,
        governance_distribution=0.70,
        liquidity_depth=0.60
    )
    assert 0 <= score <= 100
    assert isinstance(score, float)
```

### Go Tests

```go
// Table-driven test pattern
func TestTVLCalculation(t *testing.T) {
    tests := []struct {
        name     string
        values   []float64
        expected float64
    }{
        {"stable", []float64{100, 101, 99, 100}, 100.0},
        {"volatile", []float64{100, 50, 150, 80}, 95.0},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := CalculateMean(tt.values)
            if math.Abs(result-tt.expected) > 0.01 {
                t.Errorf("got %f, want %f", result, tt.expected)
            }
        })
    }
}
```

### Frontend Tests

```typescript
// Component test pattern
import { render, screen } from '@testing-library/react';
import { RiskGauge } from '@/components/risk-gauge';

test('displays risk score with correct color', () => {
  render(<RiskGauge score={85} />);
  const gauge = screen.getByTestId('risk-gauge');
  expect(gauge).toHaveClass('text-green-500');
});
```

## Code Review Checklist

When reviewing changes:

- [ ] No hardcoded API keys or secrets
- [ ] No `Math.random()` for data — use real calculations
- [ ] No "mock", "simulated", "demo", "placeholder" strings
- [ ] All functions have real implementation (no stubs)
- [ ] Type hints in Python, strict types in TypeScript
- [ ] Error handling with proper error messages
- [ ] Tests added for new functionality
- [ ] Documentation updated for API changes
- [ ] Configuration values in config files, not hardcoded
- [ ] Logging at appropriate levels

## File Modification Guide

### Modifying Risk Formula

1. Edit `src/engine/risk_scorer.py` — update computation
2. Edit `config/default.yaml` — update weights if changed
3. Edit `docs/RISK_MODEL.md` — update documentation
4. Edit `README.md` — update formula display
5. Run `make test-engine` to verify

### Adding a New Protocol

1. Add to `src/engine/protocol_registry.py`
2. Add chain info to `config/chains.yaml`
3. Run `make db-seed` to update database
4. Verify in frontend dashboard

### Modifying Frontend

1. Components are in `src/web/components/`
2. Pages are in `src/web/app/`
3. Use shadcn/ui components from `src/web/components/ui/`
4. Charts use Recharts library
5. Run `npm run dev` for hot reload

## Environment Variables

```bash
# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/defi_monitor
REDIS_URL=redis://localhost:6379

# API Keys (optional, free tiers work without)
DEFILLAMA_API_KEY=         # Optional
COINGECKO_API_KEY=         # Optional for free tier

# Scanner
SCANNER_INTERVAL=300       # Seconds between scans
SCANNER_CHAINS=ethereum,arbitrum,polygon

# Engine
ENGINE_PORT=8000
ENGINE_HOST=0.0.0.0
LOG_LEVEL=info
```
