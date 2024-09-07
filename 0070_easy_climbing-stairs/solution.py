class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0] * (n+1)
        
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
    

class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        pre = 2
        pre_pre = 1
        
        result = None
        for _ in range(3, n + 1):
            result = pre + pre_pre
            pre_pre = pre
            pre = result
            
        return result
    

from functools import lru_cache


class Solution3:

    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    

class Solution4:

    def __init__(self):
        self.cache = dict()

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        if n not in self.cache:
            self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.cache[n]