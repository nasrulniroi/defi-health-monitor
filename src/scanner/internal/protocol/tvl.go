package protocol

import "math"

type TVLMetrics struct {
	Current  float64 `json:"current"`
	Mean7d   float64 `json:"mean_7d"`
	StdDev7d float64 `json:"stddev_7d"`
	CV7d     float64 `json:"cv_7d"`
	Change7d float64 `json:"change_7d"`
}

func CalculateTVLMetrics(tvls []float64) TVLMetrics {
	if len(tvls) == 0 {
		return TVLMetrics{}
	}
	current := tvls[len(tvls)-1]
	recent := tvls
	if len(tvls) > 7 {
		recent = tvls[len(tvls)-7:]
	}
	sum := 0.0
	for _, v := range recent {
		sum += v
	}
	mean := sum / float64(len(recent))
	variance := 0.0
	for _, v := range recent {
		variance += (v - mean) * (v - mean)
	}
	stddev := math.Sqrt(variance / float64(len(recent)))
	cv := 0.0
	if mean > 0 {
		cv = stddev / mean
	}
	change := 0.0
	if len(tvls) > 7 && tvls[0] > 0 {
		change = (current - tvls[len(tvls)-7]) / tvls[len(tvls)-7]
	}
	return TVLMetrics{Current: current, Mean7d: mean, StdDev7d: stddev, CV7d: cv, Change7d: change}
}
