from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 5000
        
        if l == 1:
            return nums[0]
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        mid = l//2
        return min(self.findMin(nums[:mid]), self.findMin(nums[mid:]))