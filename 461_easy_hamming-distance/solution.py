class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x^y
        b = "%s" % bin(a)
        return b.count("1")