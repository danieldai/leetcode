import sys

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        d = dungeon
        
        m = len(d)
        n = len(d[0])
        
        dp = [[sys.maxsize] * (n + 1) for _ in range(m+1)]
        
        dp[m][n-1] = dp[m-1][n] = 1
        
        # print(dp)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(1, (min(dp[i+1][j], dp[i][j+1]) - d[i][j]))
                # print(i, j, dp[i][j])
                
        # print(dp)
        return dp[0][0]        