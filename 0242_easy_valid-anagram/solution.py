class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = dict()
        
        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
                
        for c in t:
            if c not in chars:
                return False
            else:
                chars[c] -= 1
        
        for v in chars.values():
            if v != 0:
                return False
        
        return True
        