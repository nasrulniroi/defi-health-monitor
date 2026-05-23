import pytest
import numpy as np
from src.engine.tvl_analyzer import TVLAnalyzer

@pytest.fixture
def analyzer():
    return TVLAnalyzer()

def test_stable_tvl_high_score(analyzer):
    history = [{"totalLiquidityUSD": 1000000000} for _ in range(30)]
    score = analyzer.calculate_stability(history)
    assert score > 0.8

def test_volatile_tvl_low_score(analyzer):
    history = [{"totalLiquidityUSD": 1000000000 * (1 + 0.5 * (1 if i % 2 == 0 else -1))} for i in range(30)]
    score = analyzer.calculate_stability(history)
    assert score < 0.8

def test_growing_tvl_bonus(analyzer):
    history = [{"totalLiquidityUSD": 1000000000 + (i * 50000000)} for i in range(30)]
    score = analyzer.calculate_stability(history)
    assert score > 0.5

def test_empty_history(analyzer):
    score = analyzer.calculate_stability([])
    assert score == 0.5

def test_short_history(analyzer):
    score = analyzer.calculate_stability([{"totalLiquidityUSD": 100}] * 3)
    assert score == 0.5

def test_whale_withdrawal_detection(analyzer):
    history = [{"totalLiquidityUSD": 1000000000}] * 20
    history.append({"totalLiquidityUSD": 500000000})
    withdrawals = analyzer.detect_whale_withdrawals(history)
    assert len(withdrawals) > 0
    assert withdrawals[0]["drop_pct"] > 10
