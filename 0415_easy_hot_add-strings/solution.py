class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ''

        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1

        while i >= 0 or j >= 0 or carry:
            a = int(num1[i]) if i >=0 else 0
            b = int(num2[j]) if j >=0 else 0
            result = str((a+b+carry) % 10) + result
            carry = (a+b+carry) // 10
            i -= 1
            j -= 1
        
        return result
        