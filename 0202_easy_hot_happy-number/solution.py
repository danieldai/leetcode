class Solution:
    def isHappy(self, n: int) -> bool:
        records = set()

        while n not in records and n != 1:
            records.add(n)
            n = sum([int(a)**2 for a in str(n)])
        
        return n == 1

        