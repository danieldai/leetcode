from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        return sorted([n*n for n in nums])
    

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [0] * n
        source = [i**2 for i in nums]

        i = 0
        j = n - 1

        k = n - 1
        while i <= j: # 要注意换个边界条件，当 i==j 时，其实还剩最后一个值没有取出
            if source[i] > source[j]:
                result[k] = source[i]
                i += 1
            else:
                result[k] = source[j]
                j -= 1
            k -= 1

        return result
        