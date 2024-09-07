class Solution:
    def reverse(self, x: int) -> int:
        low = -2**31-1
        high = 2**31
        
        
        if x < 0:
            s = -int(str(-x)[::-1])
            return s if s >= low else 0
        else:
            s = int(str(x)[::-1])
            return s if s <= high else 0
        

class Solution:
    def reverse(self, x: int) -> int:
        low = -2**31-1
        high = 2**31
        result = 0
        s = 1
        if x < 0:
           s = -1
           x = -x

        while x > 0:
            result = result * 10 + x % 10
            x = x // 10

        if  low <= s*result <= high:
            return s*result
        else:
            return 0

# 之上的解法都使用了超过4个字节范围的数，所以是不满足题目要求的
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 -1
        
        result = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10

            if result > (INT_MAX - digit) // 10:
                return 0

            result = result * 10 + digit
        
        return sign * result