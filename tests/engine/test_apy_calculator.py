import pytest
from src.engine.apy_calculator import APYCalculator

@pytest.fixture
def calculator():
    return APYCalculator()

def test_stable_apy_high_score(calculator):
    protocol = {"apy": 5.0, "apyMean7d": 4.8, "apyMean30d": 4.5}
    score = calculator.calculate_sustainability(protocol)
    assert score > 0.7

def test_extreme_apy_low_score(calculator):
    protocol = {"apy": 5000, "apyMean7d": 4000, "apyMean30d": 3000}
    score = calculator.calculate_sustainability(protocol)
    assert score < 0.5

def test_zero_apy(calculator):
    protocol = {"apy": 0, "apyMean7d": 0, "apyMean30d": 0}
    score = calculator.calculate_sustainability(protocol)
    assert score == 0.5

def test_normalize_apy_ethereum(calculator):
    assert calculator.normalize_apy(3.0, "Ethereum") == 1.0
    assert calculator.normalize_apy(50.0, "Ethereum") < 1.0
