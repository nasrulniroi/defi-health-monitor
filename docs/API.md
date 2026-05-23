# API Documentation

## Risk Engine API (Port 8000)

### GET /api/protocols
Returns health scores for top protocols.

**Response:**
```json
{
  "data": [
    {
      "protocol": "Aave",
      "health_score": 82.5,
      "tvl": 12500000000,
      "chain": "Multi",
      "risk_level": "low"
    }
  ],
  "count": 50
}
```

### GET /api/protocols/{id}
Returns detailed risk data for a specific protocol.

### GET /api/risk/overview
Returns risk distribution across all protocols.

### GET /api/alerts
Returns active risk alerts.

### GET /health
Health check endpoint.

## Scanner API (Port 8081)

### GET /api/scan/results
Returns latest blockchain scan results.
