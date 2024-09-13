package dex_interface

import (
	"fmt"
	"ourobroker/backend/config"
	"ourobroker/cpp_components"
)

type DEXClient struct {
	config    *config.Config
	orderBook *cpp_components.OrderBook
}

func NewDEXClient(cfg *config.Config) *DEXClient {
	orderBook := cpp_components.NewOrderBook()
	return &DEXClient{
		config:    cfg,
		orderBook: orderBook,
	}
}

func (dc *DEXClient) FetchMarketData() MarketData {
	// Fetch data from multiple DEXs
	// ...
	return MarketData{}
}

func (dc *DEXClient) ExecuteTrade(decision Decision) error {
	// Use the order book to decide on trade execution
	success := dc.orderBook.ExecuteTrade(decision)
	if !success {
		return fmt.Errorf("trade execution failed")
	}
	return nil
}
