from typing import List


class Solution:
    def __init__(self) -> None:
        self.result = []
        self.path = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtracking(nums, [False] * len(nums))
        return self.result
        
    def backtracking(self, nums: List[int], used: List[bool]) -> None:
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            if used[i]:
                continue
            used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, used)
            self.path.pop()
            used[i] = False


if __name__ == "__main__":
    result = Solution().permuteUnique([1,1,2])
    print(result)