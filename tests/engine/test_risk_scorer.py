import pytest
import numpy as np
from src.engine.risk_scorer import RiskScorer
from src.engine.utils.config import load_config

@pytest.fixture
def scorer():
    config = load_config()
    return RiskScorer(config)

@pytest.fixture
def sample_protocol():
    return {"name": "Aave", "slug": "aave", "chain": "Multi", "category": "Lending", "tvl": 12500000000, "apy": 3.5, "apyMean7d": 3.2, "apyMean30d": 3.0, "audits": 3, "audit_links": ["a", "b", "c"], "governanceID": True, "dailyVolume": 500000000}

@pytest.fixture
def sample_tvl_history():
    base_tvl = 12000000000
    return [{"totalLiquidityUSD": base_tvl + (i * 10000000 * (1 if i % 2 == 0 else -1))} for i in range(30)]

def test_health_score_range(scorer, sample_protocol, sample_tvl_history):
    result = scorer.calculate_health_score(sample_protocol, sample_tvl_history)
    assert 0 <= result["health_score"] <= 100

def test_health_score_components(scorer, sample_protocol, sample_tvl_history):
    result = scorer.calculate_health_score(sample_protocol, sample_tvl_history)
    assert "tvl_stability" in result["components"]
    assert "apy_sustainability" in result["components"]
    assert "contract_security" in result["components"]
    assert "governance_distribution" in result["components"]
    assert "liquidity_depth" in result["components"]

def test_risk_categorization(scorer):
    assert scorer.categorize_risk(85) == "low"
    assert scorer.categorize_risk(60) == "medium"
    assert scorer.categorize_risk(35) == "high"
    assert scorer.categorize_risk(10) == "critical"

def test_low_tvl_protocol(scorer):
    protocol = {"name": "TinyDEX", "slug": "tiny", "tvl": 50000, "apy": 5, "audits": 0}
    tvl_history = [{"totalLiquidityUSD": 50000 + (i * 1000) for i in range(30)}]
    result = scorer.calculate_health_score(protocol, tvl_history)
    assert result["health_score"] < 75

def test_audited_protocol_higher_security(scorer):
    audited = {"name": "Safe", "slug": "safe", "tvl": 1000000000, "audits": 3, "audit_links": ["a", "b", "c"], "category": "Lending"}
    unaudited = {"name": "Risky", "slug": "risky", "tvl": 1000000000, "audits": 0, "category": "Lending"}
    assert scorer._evaluate_security(audited) > scorer._evaluate_security(unaudited)

def test_high_apy_penalty(scorer):
    normal = {"name": "Normal", "slug": "n", "apy": 5, "apyMean30d": 4.5, "tvl": 1e9, "audits": 1}
    extreme = {"name": "Extreme", "slug": "e", "apy": 5000, "apyMean30d": 4000, "tvl": 1e9, "audits": 1}
    n_result = scorer.calculate_health_score(normal, [{"totalLiquidityUSD": 1e9}] * 30)
    e_result = scorer.calculate_health_score(extreme, [{"totalLiquidityUSD": 1e9}] * 30)
    assert n_result["components"]["apy_sustainability"] > e_result["components"]["apy_sustainability"]

def test_empty_tvl_history(scorer, sample_protocol):
    result = scorer.calculate_health_score(sample_protocol, [])
    assert result["health_score"] >= 0

def test_risk_factors_populated(scorer):
    bad_protocol = {"name": "Bad", "slug": "bad", "tvl": 100000, "apy": 5000, "audits": 0, "category": "Bridge"}
    bad_tvl = [{"totalLiquidityUSD": 100000 * (1 + 0.5 * (1 if i % 2 == 0 else -1))} for i in range(30)]
    result = scorer.calculate_health_score(bad_protocol, bad_tvl)
    assert len(result["risk_factors"]) > 0
