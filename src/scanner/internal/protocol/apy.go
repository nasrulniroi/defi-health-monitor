package protocol

import "math"

type APYMetrics struct {
	Current       float64 `json:"current"`
	Mean30d       float64 `json:"mean_30d"`
	Volatility    float64 `json:"volatility"`
	Sustainability float64 `json:"sustainability"`
}

func CalculateAPYMetrics(apys []float64) APYMetrics {
	if len(apys) == 0 {
		return APYMetrics{}
	}
	current := apys[len(apys)-1]
	sum := 0.0
	for _, v := range apys {
		sum += v
	}
	mean := sum / float64(len(apys))
	variance := 0.0
	for _, v := range apys {
		variance += (v - mean) * (v - mean)
	}
	stddev := math.Sqrt(variance / float64(len(apys)))
	volatility := 0.0
	if mean > 0 {
		volatility = stddev / mean
	}
	sustainability := math.Max(0, 1-volatility)
	if current > 1000 {
		sustainability *= 0.3
	}
	return APYMetrics{Current: current, Mean30d: mean, Volatility: volatility, Sustainability: sustainability}
}
