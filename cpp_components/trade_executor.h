#ifndef TRADE_EXECUTOR_H
#define TRADE_EXECUTOR_H

#include <mutex>
#include <string>

struct Trade {
    std::string action; // "Buy", "Sell", "Hold"
    double amount;
    // Additional fields
};

class TradeExecutor {
public:
    TradeExecutor();
    bool ExecuteTrade(Trade trade);

private:
    std::mutex execution_mutex;
};

#endif
