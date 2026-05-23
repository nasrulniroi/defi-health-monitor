package chain

import (
	"context"
	"fmt"
	"defi-health-monitor/scanner/internal/protocol"
)

type AvalancheScanner struct{}
func NewAvalancheScanner() *AvalancheScanner { return &AvalancheScanner{} }
func (a *AvalancheScanner) Name() string { return "Avalanche" }
func (a *AvalancheScanner) Scan(ctx context.Context) ([]protocol.ScanResult, error) {
	return []protocol.ScanResult{{Chain: "Avalanche", BlockNumber: 45000000, Timestamp: fmt.Sprintf("%d", 45000000), Protocols: []string{"TraderJoe", "Benqi", "Aave"}}}, nil
}
