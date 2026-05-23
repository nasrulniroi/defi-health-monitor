"""Configuration loader."""
import os
import yaml
from typing import Dict, Any

DEFAULT_CONFIG = {
    "weights": {"tvl_stability": 0.30, "apy_sustainability": 0.20, "contract_security": 0.25, "governance_distribution": 0.15, "liquidity_depth": 0.10},
    "cache_ttl": 300,
    "max_protocols": 100,
    "chains": ["Ethereum", "Arbitrum", "Polygon", "BSC", "Avalanche", "Optimism", "Fantom", "Solana"],
    "risk_thresholds": {"critical": 25, "high": 50, "medium": 75},
}

def load_config(path: str = None) -> Dict[str, Any]:
    if path and os.path.exists(path):
        with open(path) as f:
            user_config = yaml.safe_load(f)
            if user_config:
                merged = DEFAULT_CONFIG.copy()
                merged.update(user_config)
                return merged
    return DEFAULT_CONFIG
