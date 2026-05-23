#!/bin/bash
set -euo pipefail
echo "Setting up DeFi Health Monitor..."
pip install -r requirements.txt 2>/dev/null || pip install fastapi uvicorn aiohttp numpy scipy pyyaml
cd src/scanner && go mod tidy 2>/dev/null || true
cd ../web && npm install 2>/dev/null || true
echo "Setup complete."
