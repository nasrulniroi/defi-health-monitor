import pytest
from src.engine.anomaly_detector import AnomalyDetector

@pytest.fixture
def detector():
    return AnomalyDetector()

def test_no_anomalies_stable_data(detector):
    history = [{"totalLiquidityUSD": 1000000000}] * 30
    anomalies = detector.detect(history)
    assert len(anomalies) == 0

def test_detect_spike(detector):
    history = [{"totalLiquidityUSD": 1000000000}] * 20
    history.append({"totalLiquidityUSD": 5000000000})
    anomalies = detector.detect(history)
    assert len(anomalies) > 0

def test_short_data_no_crash(detector):
    anomalies = detector.detect([{"totalLiquidityUSD": 100}] * 5)
    assert anomalies == []

def test_rapid_change_detection(detector):
    history = [{"totalLiquidityUSD": 1000000000}] * 10
    history.append({"totalLiquidityUSD": 500000000})
    changes = detector.detect_rapid_changes(history, threshold=0.2)
    assert len(changes) > 0
