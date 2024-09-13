package main

import (
	"encoding/json"
	"net/http"
	"sync"
)

type Metrics struct {
	TotalTrades       int     `json:"total_trades"`
	SuccessfulTrades  int     `json:"successful_trades"`
	FailedTrades      int     `json:"failed_trades"`
	CurrentExposure   float64 `json:"current_exposure"`
	ProfitAndLoss     float64 `json:"profit_and_loss"`
	LiquidityProvided float64 `json:"liquidity_provided"`
}

var (
	metrics      Metrics
	metricsMutex sync.RWMutex
)

func metricsHandler(w http.ResponseWriter, r *http.Request) {
	metricsMutex.RLock()
	defer metricsMutex.RUnlock()
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(metrics)
}

func main() {
	http.HandleFunc("/api/metrics", metricsHandler)
	http.ListenAndServe(":8080", nil)
}
