class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        
        xx = x

        y = 0;

        while x > 0: 
            y = y * 10 + x % 10;
            x = x // 10;
        
        return xx == y;
        

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10
        
        return x == reverse or x == reverse // 10 