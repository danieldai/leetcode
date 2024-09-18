from typing import List


class Solution:

    def __init__(self) -> None:
        self.result = []
        self.path = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums: List[int], start_index: int) -> None:
        if len(self.path) >= 2:
            self.result.append(self.path[:])
        
        if start_index >= len(nums):
            return
        
        used_nums = set()
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] in used_nums:
                continue 
            if self.path and nums[i] < self.path[-1]:
                continue
            used_nums.add(nums[i])
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()



if __name__ == "__main__":
    result = Solution().findSubsequences([4,6,7,7])
    print(result)

    