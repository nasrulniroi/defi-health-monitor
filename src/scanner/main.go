package main

import (
	"fmt"
	"os"
	"defi-health-monitor/scanner/cmd"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: scanner <scan|serve>")
		os.Exit(1)
	}
	switch os.Args[1] {
	case "scan":
		cmd.RunScan()
	case "serve":
		cmd.RunServe()
	default:
		fmt.Printf("Unknown command: %s\n", os.Args[1])
		os.Exit(1)
	}
}
