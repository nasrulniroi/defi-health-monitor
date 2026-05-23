package chain

import (
	"context"
	"fmt"
	"defi-health-monitor/scanner/internal/protocol"
)

type OptimismScanner struct{}
func NewOptimismScanner() *OptimismScanner { return &OptimismScanner{} }
func (o *OptimismScanner) Name() string { return "Optimism" }
func (o *OptimismScanner) Scan(ctx context.Context) ([]protocol.ScanResult, error) {
	return []protocol.ScanResult{{Chain: "Optimism", BlockNumber: 120000000, Timestamp: fmt.Sprintf("%d", 120000000), Protocols: []string{"Velodrome", "Aave", "Synthetix"}}}, nil
}
