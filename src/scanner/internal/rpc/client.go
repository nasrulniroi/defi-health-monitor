package rpc

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
	"time"
)

type RPCClient struct {
	Endpoint string
	Client   *http.Client
}

func NewRPCClient(endpoint string) *RPCClient {
	return &RPCClient{Endpoint: endpoint, Client: &http.Client{Timeout: 30 * time.Second}}
}

func (r *RPCClient) GetBlockNumber(ctx context.Context) (int64, error) {
	payload := `{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}`
	req, _ := http.NewRequestWithContext(ctx, "POST", r.Endpoint, strings.NewReader(payload))
	req.Header.Set("Content-Type", "application/json")
	resp, err := r.Client.Do(req)
	if err != nil {
		return 0, fmt.Errorf("RPC call failed: %w", err)
	}
	defer resp.Body.Close()
	var result struct {
		Result string `json:"result"`
	}
	json.NewDecoder(resp.Body).Decode(&result)
	var blockNum int64
	fmt.Sscanf(result.Result, "0x%x", &blockNum)
	return blockNum, nil
}
