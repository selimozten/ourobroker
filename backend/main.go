package main

import (
	"fmt"
	"log"

	"ourobroker/backend/config"
	"ourobroker/backend/dex_interface"
	"ourobroker/backend/order_manager"
	"ourobroker/backend/risk_monitor"
)

func main() {
	cfg, err := config.LoadConfig("configs/config.yaml")
	if err != nil {
		log.Fatalf("Failed to load config: %v", err)
	}

	dexClient := dex_interface.NewDEXClient(cfg)
	orderMgr := order_manager.NewOrderManager(dexClient)
	riskMon := risk_monitor.NewRiskMonitor(cfg)

	// Start the backend services
	go orderMgr.Start()
	go riskMon.Start()

	fmt.Println("AI Market Maker Backend is running...")
	select {}
}
