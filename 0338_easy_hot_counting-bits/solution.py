from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)
        for i in range(1, n+1):
            bits[i] = bits[i&(i-1)] + 1
        
        return bits
    
    # 如果一个数是奇数，那么它的1的个数为 n-1 的 1的个数加1
    # 如果一个数是偶数，那么它的1的个数为 为 n/2 的 1的个数相同
    def countBits2(self, n: int) -> List[int]:
        bits = [0] * (n + 1)

        for i in range(1, n+1):
            bits[i] = bits[i-1] + 1 if i&1 else bits[i>>1]
        
        return bits
