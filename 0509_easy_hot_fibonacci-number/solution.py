class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        pre_pre = 0
        pre = 1

        result = 0
        for _ in range(2, n+1):
            result = pre_pre + pre
            pre_pre = pre
            pre = result
        
        return result