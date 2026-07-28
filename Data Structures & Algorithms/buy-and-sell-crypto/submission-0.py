class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_hold_profit = -prices[0]
        max_not_hold_profit = 0

        for i in range(1, len(prices)):
            max_hold_profit = max(max_hold_profit, -prices[i])
            max_not_hold_profit = max(max_not_hold_profit, max_hold_profit + prices[i])
        
        return max_not_hold_profit