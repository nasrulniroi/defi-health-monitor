#!/bin/bash
set -euo pipefail
echo "Deploying DeFi Health Monitor..."
cd src/web && npm run build
echo "Build complete. Deploy to hosting provider."
