package protocol

type ScanResult struct {
	Chain     string   `json:"chain"`
	BlockNumber int64  `json:"block_number"`
	Timestamp string   `json:"timestamp"`
	Protocols []string `json:"protocols"`
}

var latestResults []ScanResult

func GetLatestResults() []ScanResult {
	return latestResults
}

func SetLatestResults(results []ScanResult) {
	latestResults = results
}
