def buy_and_sell_stock_once(prices):
    min_price = float('inf')
    max_profit = 0.0

    for price in prices:
        min_price = min(price, min_price)
        max_profit_today = price - min_price
        max_profit = max(max_profit, max_profit_today)

    return max_profit


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main("buy_and_sell_stock.tsv",
                                              buy_and_sell_stock_once)
