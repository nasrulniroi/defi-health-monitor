import pytest
from src.engine.risk_scorer import RiskScorer
from src.engine.tvl_analyzer import TVLAnalyzer
from src.engine.apy_calculator import APYCalculator
from src.engine.anomaly_detector import AnomalyDetector
from src.engine.protocol_registry import ProtocolRegistry
from src.engine.data.cache import Cache
from src.engine.utils.config import load_config

def test_full_pipeline():
    config = load_config()
    scorer = RiskScorer(config)
    protocol = {"name": "Aave", "slug": "aave", "chain": "Multi", "category": "Lending", "tvl": 12500000000, "apy": 3.5, "apyMean7d": 3.2, "apyMean30d": 3.0, "audits": 3, "audit_links": ["a", "b", "c"], "governanceID": True, "dailyVolume": 500000000}
    tvl_history = [{"totalLiquidityUSD": 12000000000 + (i * 10000000 * (1 if i % 2 == 0 else -1))} for i in range(30)]
    result = scorer.calculate_health_score(protocol, tvl_history)
    assert "health_score" in result
    assert "components" in result
    assert "risk_level" in result
    assert result["protocol"] == "Aave"

def test_registry_integration():
    registry = ProtocolRegistry()
    registry.register("aave", {"name": "Aave", "chain": "Multi", "category": "Lending"})
    assert registry.get("aave") is not None
    assert len(registry.get_all()) == 1

def test_cache_integration():
    cache = Cache(ttl=60)
    cache.set("test_key", {"value": 42})
    assert cache.get("test_key") == {"value": 42}
    assert cache.get("missing") is None
    assert cache.size() == 1
