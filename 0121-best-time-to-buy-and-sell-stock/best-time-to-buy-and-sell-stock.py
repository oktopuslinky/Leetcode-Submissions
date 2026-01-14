class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy_price = prices[0]
        profit = 0

        for price in prices:
            if price < buy_price:
                buy_price = price
                continue

            profit = max(profit, price-buy_price)
        
        return profit