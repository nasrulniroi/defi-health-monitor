package cmd

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"
	"defi-health-monitor/scanner/internal/protocol"
)

func RunServe() {
	http.HandleFunc("/api/scan/results", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.Header().Set("Access-Control-Allow-Origin", "*")
		results := protocol.GetLatestResults()
		json.NewEncoder(w).Encode(map[string]interface{}{"data": results, "timestamp": time.Now().Unix()})
	})
	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
	})
	fmt.Println("Scanner API server running on :8081")
	log.Fatal(http.ListenAndServe(":8081", nil))
}
