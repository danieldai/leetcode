from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)

        a = nums[0] * nums[1]
        b = nums[-2] * nums[-1]

        
        return max(a * nums[-1], b * nums[-3])