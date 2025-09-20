class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        start = prices[0]
        days = len(prices)
        for day in range(1,days):
            if prices[day]>start:
                max_profit += prices[day]-start
            start = prices[day]
        return max_profit
            