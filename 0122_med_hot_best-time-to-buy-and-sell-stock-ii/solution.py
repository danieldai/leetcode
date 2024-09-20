from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        n = len(prices)
        
        # dp[i][0] 表示第i天不持有股票，可能是昨天持有今天卖出，或者昨天也没有持有
        # dp[i][1] 表示第i天持有股票，可能昨天没有持有今天买入，或者昨天也没有持有
        dp = [[0, 0] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        
        return dp[n-1][0]