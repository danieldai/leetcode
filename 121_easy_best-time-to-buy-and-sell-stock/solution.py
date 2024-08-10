from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        
        high = prices[-1]

        for i in range(n-2, -1, -1):
            res = max(res, high - prices[i])
            high = max(high, prices[i])
            
        return res