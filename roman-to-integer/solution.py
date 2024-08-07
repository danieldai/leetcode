class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        num = digits[s[-1]]
        last = digits[s[-1]]
        for d in s[-2::-1]:
            if digits[d] < last:
                num -= digits[d]
            else:
                num += digits[d]
            last = digits[d]
        return num