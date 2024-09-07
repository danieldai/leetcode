from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] = self.nums[i] + self.nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        n1 = n2 = 0
        if left > 0:
            n1 = self.nums[left-1]
        n2 = self.nums[right]
        return n2 - n1
            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


class NumArray2:

    def __init__(self, nums: List[int]):
        self.nums = [0] + nums
        for i in range(1, len(nums) + 1):
            self.nums[i] = self.nums[i] + self.nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1] - self.nums[left]
            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)