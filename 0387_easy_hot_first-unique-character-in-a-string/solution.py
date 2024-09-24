class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = dict()
        idx = []

        for i, c in enumerate(s):
            if c not in chars:
                chars[c] = 1
                idx.append(i)
            else:
                chars[c] += 1

        for i in idx:
            if chars[s[i]] == 1:
                return i
        
        return -1
        
        
