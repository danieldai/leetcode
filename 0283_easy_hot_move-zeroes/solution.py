from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                self.moveZeroToRight(nums, i)

    def moveZeroToRight(self, nums: List[int], position) -> None:
        for i in range(position, len(nums)-1):
            if nums[i+1] != 0:
                nums[i], nums[i+1] = nums[i+1], nums[i]


class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        i = 0
        while i < len(nums) and nums[i] != 0:
            i += 1

        for j in range(i, len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        for j in range(i, len(nums)):
            nums[j] = 0