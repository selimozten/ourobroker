package order_manager

import (
	"log"
	"ourobroker/backend/dex_interface"
	"ourobroker/ml_models"
)

type OrderManager struct {
	dexClient *dex_interface.DEXClient
	aiModel   *ml_models.Model
}

func NewOrderManager(dexClient *dex_interface.DEXClient) *OrderManager {
	model := ml_models.LoadModel("ml_models/model_weights.pth")
	return &OrderManager{
		dexClient: dexClient,
		aiModel:   model,
	}
}

func (om *OrderManager) Start() {
	// Main loop to fetch market data and make trading decisions
	for {
		marketData := om.dexClient.FetchMarketData()
		decision := om.aiModel.Predict(marketData)
		if decision.ShouldTrade {
			err := om.dexClient.ExecuteTrade(decision)
			if err != nil {
				log.Printf("Trade execution failed: %v", err)
			}
		}
		// Sleep or wait for the next data update
	}
}
