from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        s = ' ' + s
        f = [0] * len(s)
        
        f[0] = 1
        
        for i in range(1, n+1):
            for j in range(0, i):
                if f[j] and s[j+1:i+1] in words:
                    f [i] = 1
                    break
        return f[n] == 1