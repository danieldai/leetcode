from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = Counter(ransomNote)
        b = Counter(magazine)

        for k in a.keys():
            if k not in b or a[k] > b[k]:
                return False

        return True 
        