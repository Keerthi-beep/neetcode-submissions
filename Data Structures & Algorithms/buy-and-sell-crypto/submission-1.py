class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=float('-inf')
        n=len(prices)
        for i in range(n):
            for j in range(i+1,n):
                max_profit=max(max_profit,prices[j]-prices[i])
        return max_profit if max_profit>0 else 0 