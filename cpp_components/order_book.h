#ifndef ORDER_BOOK_H
#define ORDER_BOOK_H

#include <vector>
#include <mutex>

struct Decision {
    int action;  // 0: Buy, 1: Sell, 2: Hold
    // Additional fields
};

class OrderBook {
public:
    OrderBook();
    bool ExecuteTrade(Decision decision);

private:
    std::vector<int> bids;
    std::vector<int> asks;
    std::mutex order_book_mutex;
};

#endif
