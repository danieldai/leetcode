class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        s = 1
        if num < 0:
            s = -1
            num = s * num
        
        result = ""

        while num > 0:
            r = num % 7
            num = num // 7
            result = str(r) + result
        
        if s < 0:
            result = '-' + result
        return result
        