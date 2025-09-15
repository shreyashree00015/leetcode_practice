class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_value = inf
        max_profit = 0
        for i in prices:
            least_value = min(i,least_value)
            current_profit = i - least_value
            max_profit = max(current_profit, max_profit)

        return max_profit