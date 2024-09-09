class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x^y
        result = 0

        while a:
            result += 1
            a = a & (a - 1)

        return result