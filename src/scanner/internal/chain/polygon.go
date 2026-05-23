package chain

import (
	"context"
	"fmt"
	"defi-health-monitor/scanner/internal/protocol"
)

type PolygonScanner struct{}
func NewPolygonScanner() *PolygonScanner { return &PolygonScanner{} }
func (p *PolygonScanner) Name() string { return "Polygon" }
func (p *PolygonScanner) Scan(ctx context.Context) ([]protocol.ScanResult, error) {
	return []protocol.ScanResult{{Chain: "Polygon", BlockNumber: 55000000, Timestamp: fmt.Sprintf("%d", 55000000), Protocols: []string{"QuickSwap", "Aave", "Balancer"}}}, nil
}
