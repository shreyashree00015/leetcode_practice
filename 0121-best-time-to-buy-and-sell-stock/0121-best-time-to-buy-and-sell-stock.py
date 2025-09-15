class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_val = inf
        max_profit = 0
        for i in prices:
            least_val = min(i,least_val)
            current_profit = i-least_val
            max_profit = max(max_profit,current_profit)
        return(max_profit)