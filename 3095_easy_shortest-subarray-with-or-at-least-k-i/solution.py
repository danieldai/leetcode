from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 51
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                sum_or = 0
                for idx in range(i, j + 1): 
                    sum_or |= nums[idx]
                if sum_or >= k: 
                    res = min(res, j - i + 1)
        return res if res != 51 else -1   