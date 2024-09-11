from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        
        n = len(nums)

        i = n - 1
        while i >= 0 and nums[i] == val:
            i -= 1
            
        for j in range(i - 1, -1, -1):
            if nums[j] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i -= 1

        return i + 1

