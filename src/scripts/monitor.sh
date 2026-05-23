#!/bin/bash
set -euo pipefail
while true; do
  echo "[$(date)] Running health check..."
  curl -sf http://localhost:8000/health > /dev/null && echo "Engine: OK" || echo "Engine: DOWN"
  curl -sf http://localhost:8081/health > /dev/null && echo "Scanner: OK" || echo "Scanner: DOWN"
  sleep 60
done
