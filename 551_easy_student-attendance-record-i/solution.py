class Solution:
    def checkRecord(self, s: str) -> bool:
        A = 0
        L = 0

        for c in s:
            if c == 'A':
                A += 1
                L = 0
            if c == 'L':
                L += 1
            if c == 'P':
                L = 0
            if A >= 2 or L >= 3:
                return False
        
        return True