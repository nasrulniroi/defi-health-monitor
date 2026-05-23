#!/bin/bash
set -euo pipefail
ENGINE=$(curl -sf http://localhost:8000/health 2>/dev/null | grep -c ok || echo 0)
SCANNER=$(curl -sf http://localhost:8081/health 2>/dev/null | grep -c ok || echo 0)
if [ "$ENGINE" -eq 1 ] && [ "$SCANNER" -eq 1 ]; then
  echo "All services healthy"
  exit 0
else
  echo "Service health check failed: engine=$ENGINE scanner=$SCANNER"
  exit 1
fi
