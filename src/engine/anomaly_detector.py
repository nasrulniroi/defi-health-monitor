"""Statistical anomaly detection for TVL and APY data."""
import numpy as np
from typing import Dict, List

class AnomalyDetector:
    def detect(self, tvl_history: List[Dict], z_threshold: float = 2.5) -> List[Dict]:
        if not tvl_history or len(tvl_history) < 10:
            return []
        tvls = [entry.get("totalLiquidityUSD", entry.get("tvl", 0)) for entry in tvl_history]
        tvls = np.array([t for t in tvls if t > 0], dtype=float)
        if len(tvls) < 10:
            return []
        mean = np.mean(tvls)
        std = np.std(tvls)
        if std <= 0:
            return []
        z_scores = np.abs((tvls - mean) / std)
        anomalies = []
        for i, z in enumerate(z_scores):
            if z > z_threshold:
                anomalies.append({"index": int(i), "z_score": round(float(z), 2), "tvl": float(tvls[i]), "expected": round(float(mean), 2), "deviation_pct": round(float((tvls[i] - mean) / mean * 100), 2)})
        return anomalies

    def detect_rapid_changes(self, tvl_history: List[Dict], threshold: float = 0.2) -> List[Dict]:
        changes = []
        for i in range(1, len(tvl_history)):
            prev = tvl_history[i-1].get("totalLiquidityUSD", 0)
            curr = tvl_history[i].get("totalLiquidityUSD", 0)
            if prev > 0:
                change = abs(curr - prev) / prev
                if change > threshold:
                    changes.append({"index": i, "change_pct": round(change * 100, 2), "direction": "increase" if curr > prev else "decrease"})
        return changes
