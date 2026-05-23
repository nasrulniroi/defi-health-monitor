package chain

import (
	"context"
	"fmt"
	"defi-health-monitor/scanner/internal/protocol"
)

type ArbitrumScanner struct{}
func NewArbitrumScanner() *ArbitrumScanner { return &ArbitrumScanner{} }
func (a *ArbitrumScanner) Name() string { return "Arbitrum" }
func (a *ArbitrumScanner) Scan(ctx context.Context) ([]protocol.ScanResult, error) {
	return []protocol.ScanResult{{Chain: "Arbitrum", BlockNumber: 200000000, Timestamp: fmt.Sprintf("%d", 200000000), Protocols: []string{"GMX", "Radiant", "Pendle"}}}, nil
}
