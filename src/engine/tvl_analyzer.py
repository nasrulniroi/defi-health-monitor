"""TVL trend analysis and stability scoring."""
import numpy as np
from typing import Dict, List

class TVLAnalyzer:
    def calculate_stability(self, tvl_history: List[Dict]) -> float:
        if not tvl_history or len(tvl_history) < 7:
            return 0.5
        tvls = [entry.get("totalLiquidityUSD", entry.get("tvl", 0)) for entry in tvl_history]
        tvls = [t for t in tvls if t > 0]
        if len(tvls) < 7:
            return 0.5
        mean_tvl = np.mean(tvls)
        std_tvl = np.std(tvls)
        if mean_tvl <= 0:
            return 0.0
        cv = std_tvl / mean_tvl
        stability = max(0, 1 - cv)
        recent = tvls[-7:]
        older = tvls[-14:-7] if len(tvls) >= 14 else tvls[:7]
        if np.mean(older) > 0:
            trend = (np.mean(recent) - np.mean(older)) / np.mean(older)
            trend_factor = min(1.0, max(0.0, 0.5 + trend))
            stability = 0.7 * stability + 0.3 * trend_factor
        return min(1.0, max(0.0, stability))

    def detect_whale_withdrawals(self, tvl_history: List[Dict], threshold: float = 0.1) -> List[Dict]:
        withdrawals = []
        for i in range(1, len(tvl_history)):
            prev = tvl_history[i-1].get("totalLiquidityUSD", 0)
            curr = tvl_history[i].get("totalLiquidityUSD", 0)
            if prev > 0:
                change = (prev - curr) / prev
                if change > threshold:
                    withdrawals.append({"index": i, "drop_pct": round(change * 100, 2), "tvl_before": prev, "tvl_after": curr})
        return withdrawals
