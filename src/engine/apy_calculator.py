"""APY sustainability analysis."""
import numpy as np
from typing import Dict, List, Any

class APYCalculator:
    def calculate_sustainability(self, protocol: Dict) -> float:
        apy = protocol.get("apy", protocol.get("apyMean30d", 0))
        apy_30d = protocol.get("apyMean30d", apy)
        apy_7d = protocol.get("apyMean7d", apy)
        if apy <= 0 and apy_30d <= 0:
            return 0.5
        if apy > 0 and apy_30d > 0:
            deviation = abs(apy - apy_30d) / max(apy_30d, 1)
            sustainability = max(0, 1 - deviation)
        else:
            sustainability = 0.5
        if apy > 1000:
            sustainability *= 0.3
        elif apy > 500:
            sustainability *= 0.5
        elif apy > 200:
            sustainability *= 0.7
        if apy_7d > 0 and apy_30d > 0:
            volatility = abs(apy_7d - apy_30d) / max(apy_30d, 1)
            if volatility > 0.5:
                sustainability *= 0.6
        return min(1.0, max(0.0, sustainability))

    def normalize_apy(self, apy: float, chain: str = "Ethereum") -> float:
        chain_benchmarks = {"Ethereum": 4.0, "Arbitrum": 5.0, "Polygon": 6.0, "BSC": 8.0, "Avalanche": 7.0, "Optimism": 5.0, "Solana": 8.0}
        benchmark = chain_benchmarks.get(chain, 5.0)
        if apy <= benchmark * 2:
            return 1.0
        excess = apy - benchmark * 2
        penalty = min(0.8, excess / (benchmark * 10))
        return max(0.2, 1.0 - penalty)
