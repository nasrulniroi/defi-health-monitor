#!/bin/bash
set -euo pipefail
BACKUP_DIR="backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
cp -r src/engine/data/*.py "$BACKUP_DIR/" 2>/dev/null || true
echo "Backup saved to $BACKUP_DIR"
