package scanner

import (
	"testing"
	"defi-health-monitor/scanner/internal/protocol"
)

func TestCalculateTVLMetrics(t *testing.T) {
	tvls := []float64{1000, 1050, 980, 1020, 990, 1010, 1000}
	metrics := protocol.CalculateTVLMetrics(tvls)
	if metrics.Current != 1000 {
		t.Errorf("Expected current TVL 1000, got %f", metrics.Current)
	}
	if metrics.Mean7d <= 0 {
		t.Error("Expected positive mean")
	}
}

func TestCalculateAPYMetrics(t *testing.T) {
	apys := []float64{5.0, 5.2, 4.8, 5.1, 4.9, 5.0, 5.1}
	metrics := protocol.CalculateAPYMetrics(apys)
	if metrics.Current != 5.1 {
		t.Errorf("Expected current APY 5.1, got %f", metrics.Current)
	}
	if metrics.Sustainability <= 0 || metrics.Sustainability > 1 {
		t.Errorf("Expected sustainability between 0 and 1, got %f", metrics.Sustainability)
	}
}

func TestEmptyTVL(t *testing.T) {
	metrics := protocol.CalculateTVLMetrics([]float64{})
	if metrics.Current != 0 {
		t.Error("Expected zero for empty TVL")
	}
}

func TestExtremeAPYPenalty(t *testing.T) {
	normal := protocol.CalculateAPYMetrics([]float64{5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0})
	extreme := protocol.CalculateAPYMetrics([]float64{5000.0, 5000.0, 5000.0, 5000.0, 5000.0, 5000.0, 5000.0})
	if normal.Sustainability <= extreme.Sustainability {
		t.Error("Normal APY should have higher sustainability than extreme APY")
	}
}
