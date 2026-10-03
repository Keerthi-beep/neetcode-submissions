class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        res=0
        for i in prices:
            min_price=min(min_price,i)
            res=max(i-min_price,res)
        return res