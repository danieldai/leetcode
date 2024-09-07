from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in d and d[complement] != i:
                return [i, d[complement]]
            else:
                d[num] = i