package chain

import (
	"context"
	"fmt"
	"defi-health-monitor/scanner/internal/protocol"
)

type BSCScanner struct{}
func NewBSCScanner() *BSCScanner { return &BSCScanner{} }
func (b *BSCScanner) Name() string { return "BSC" }
func (b *BSCScanner) Scan(ctx context.Context) ([]protocol.ScanResult, error) {
	return []protocol.ScanResult{{Chain: "BSC", BlockNumber: 38000000, Timestamp: fmt.Sprintf("%d", 38000000), Protocols: []string{"PancakeSwap", "Venus", "Alpaca"}}}, nil
}
