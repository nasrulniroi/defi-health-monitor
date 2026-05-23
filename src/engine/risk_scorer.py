"""Core risk scoring engine implementing the Protocol Health Score formula.

PHS = 100 * (w1*TVL_Stability + w2*APY_Sustainability + w3*Contract_Security + w4*Governance_Distribution + w5*Liquidity_Depth)
"""
import numpy as np
from typing import Dict, List, Optional, Any
from src.engine.tvl_analyzer import TVLAnalyzer
from src.engine.apy_calculator import APYCalculator
from src.engine.anomaly_detector import AnomalyDetector

WEIGHTS = {"tvl_stability": 0.30, "apy_sustainability": 0.20, "contract_security": 0.25, "governance_distribution": 0.15, "liquidity_depth": 0.10}

class RiskScorer:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.tvl_analyzer = TVLAnalyzer()
        self.apy_calculator = APYCalculator()
        self.anomaly_detector = AnomalyDetector()
        self.weights = config.get("weights", WEIGHTS)

    def calculate_health_score(self, protocol: Dict, tvl_history: List[Dict]) -> Dict[str, Any]:
        tvl_score = self.tvl_analyzer.calculate_stability(tvl_history)
        apy_score = self.apy_calculator.calculate_sustainability(protocol)
        security_score = self._evaluate_security(protocol)
        governance_score = self._evaluate_governance(protocol)
        liquidity_score = self._evaluate_liquidity(protocol)
        anomalies = self.anomaly_detector.detect(tvl_history)

        composite = (
            self.weights["tvl_stability"] * tvl_score +
            self.weights["apy_sustainability"] * apy_score +
            self.weights["contract_security"] * security_score +
            self.weights["governance_distribution"] * governance_score +
            self.weights["liquidity_depth"] * liquidity_score
        )
        health_score = round(composite * 100, 2)

        risk_factors = []
        if tvl_score < 0.3: risk_factors.append("tvl_volatility")
        if apy_score < 0.3: risk_factors.append("unsustainable_apy")
        if security_score < 0.3: risk_factors.append("low_audit_coverage")
        if governance_score < 0.3: risk_factors.append("centralized_governance")
        if liquidity_score < 0.3: risk_factors.append("low_liquidity_depth")
        if anomalies: risk_factors.append("anomaly_detected")

        return {
            "protocol": protocol.get("name", "Unknown"),
            "slug": protocol.get("slug", ""),
            "health_score": health_score,
            "components": {
                "tvl_stability": round(tvl_score, 4),
                "apy_sustainability": round(apy_score, 4),
                "contract_security": round(security_score, 4),
                "governance_distribution": round(governance_score, 4),
                "liquidity_depth": round(liquidity_score, 4),
            },
            "tvl": protocol.get("tvl", 0),
            "chain": protocol.get("chain", "Multi"),
            "category": protocol.get("category", "Unknown"),
            "risk_factors": risk_factors,
            "anomalies": anomalies,
            "risk_level": self.categorize_risk(health_score),
        }

    def categorize_risk(self, score: float) -> str:
        if score >= 75: return "low"
        if score >= 50: return "medium"
        if score >= 25: return "high"
        return "critical"

    def _evaluate_security(self, protocol: Dict) -> float:
        audits = protocol.get("audits", 0)
        audit_links = protocol.get("audit_links", [])
        if audits >= 3 and len(audit_links) >= 2: return 1.0
        if audits >= 2: return 0.8
        if audits >= 1: return 0.6
        if protocol.get("category", "").lower() in ["lending", "bridge"]: return 0.2
        return 0.4

    def _evaluate_governance(self, protocol: Dict) -> float:
        if protocol.get("governanceID"): return 0.7
        if protocol.get("treasury"): return 0.5
        return 0.3

    def _evaluate_liquidity(self, protocol: Dict) -> float:
        tvl = protocol.get("tvl", 0)
        volume = protocol.get("dailyVolume", protocol.get("volume", 0))
        if tvl <= 0: return 0.0
        ratio = volume / tvl
        if ratio >= 0.5: return 1.0
        if ratio >= 0.2: return 0.8
        if ratio >= 0.1: return 0.6
        if ratio >= 0.05: return 0.4
        return max(0.1, ratio * 4)
