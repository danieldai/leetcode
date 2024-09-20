import math


class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        for i in range(n + 1):
            for j in range(1, int(math.sqrt(n)) + 1):
                dp[i] = min(dp[i - j * j] + 1, dp[i])

        return dp[n]
        
