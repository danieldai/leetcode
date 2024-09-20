from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        s = ' ' + s
        dp = [0] * len(s)
        
        dp[0] = 1
        
        for i in range(1, n + 1):
            for j in range(0, i):
                if dp[j] and s[j + 1:i + 1] in words:
                    dp[i] = 1
                    break
        return dp[n] == 1