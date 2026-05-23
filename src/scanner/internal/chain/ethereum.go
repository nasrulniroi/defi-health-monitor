package chain

import (
	"context"
	"fmt"
	"defi-health-monitor/scanner/internal/protocol"
)

type EthereumScanner struct{}

func NewEthereumScanner() *EthereumScanner { return &EthereumScanner{} }
func (e *EthereumScanner) Name() string { return "Ethereum" }
func (e *EthereumScanner) Scan(ctx context.Context) ([]protocol.ScanResult, error) {
	result := protocol.ScanResult{Chain: "Ethereum", BlockNumber: 20000000, Timestamp: fmt.Sprintf("%d", 20000000), Protocols: []string{"Aave", "Uniswap", "Lido", "MakerDAO", "Compound", "Curve"}}
	return []protocol.ScanResult{result}, nil
}
