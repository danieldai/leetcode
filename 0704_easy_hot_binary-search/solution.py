from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1 and nums[0] != target:
            return -1

        mid = (len(nums) - 1) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.search(nums[:mid], target)
        else:
            ret = self.search(nums[mid + 1:], target)
            return -1 if ret == -1 else ret + mid + 1


    def search2(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) // 2

        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1 
            elif nums [mid] < target:
                left = mid + 1
            mid = left + (right - left) // 2

        return -1
