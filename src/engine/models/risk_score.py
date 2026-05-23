"""Risk score data model."""
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class RiskScore:
    protocol: str
    health_score: float
    components: Dict[str, float]
    risk_factors: List[str] = field(default_factory=list)
    risk_level: str = "unknown"
    anomalies: List[Dict] = field(default_factory=list)

    def to_dict(self) -> Dict:
        return {"protocol": self.protocol, "health_score": self.health_score, "components": self.components, "risk_factors": self.risk_factors, "risk_level": self.risk_level, "anomalies": self.anomalies}
