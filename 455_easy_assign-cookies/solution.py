from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        i = j = 0

        result = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                result += 1
            elif g[i] > s[j]:
                j += 1

        return result
        
        