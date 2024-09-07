from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])

        left = nums[0]
        middle = nums[len(nums)//2]
        right = nums[-1]

        if left < middle < right:
            return self.findMin(nums[:len(nums)//2])
        if middle < left and middle < right:
            return self.findMin(nums[:len(nums)//2+1])
        if middle > left and middle > right:
            return self.findMin(nums[len(nums)//2:])