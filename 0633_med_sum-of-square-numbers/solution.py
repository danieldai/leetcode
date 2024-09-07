class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        
        for i in range(1, int(c**0.5)+1):
            b = c - i**2
            if int(b**0.5)**2 == b:
                return True
        
        return False
