# Deployment Guide

## Prerequisites
- Python 3.11+
- Go 1.21+
- Node.js 18+
- PostgreSQL 15+ (optional, SQLite for local dev)

## Local Development

```bash
# Install dependencies
make setup

# Start risk engine
cd src/engine && python main.py

# Start scanner (separate terminal)
cd src/scanner && go run main.go serve

# Start frontend (separate terminal)
cd src/web && npm run dev
```

## Docker

```bash
docker-compose up -d
```

## Production

```bash
make build
make deploy
```
