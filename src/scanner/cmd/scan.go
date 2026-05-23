package cmd

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"time"
	"defi-health-monitor/scanner/internal/chain"
	"defi-health-monitor/scanner/internal/protocol"
)

func RunScan() {
	ctx, cancel := context.WithTimeout(context.Background(), 60*time.Second)
	defer cancel()
	chains := []chain.ChainScanner{
		chain.NewEthereumScanner(),
		chain.NewArbitrumScanner(),
		chain.NewPolygonScanner(),
		chain.NewBSCScanner(),
		chain.NewOptimismScanner(),
		chain.NewAvalancheScanner(),
	}
	var results []protocol.ScanResult
	for _, c := range chains {
		result, err := c.Scan(ctx)
		if err != nil {
			log.Printf("Error scanning %s: %v", c.Name(), err)
			continue
		}
		results = append(results, result...)
	}
	data, _ := json.MarshalIndent(results, "", "  ")
	fmt.Println(string(data))
}
