from typing import List


class Solution:
    def __init__(self) -> None:
        self.result = []
        self.path = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums: List[int], start_index: int) -> None:
        self.result.append(self.path[:])
        if start_index == len(nums):
            return
        
        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()


if __name__ == '__main__':
    result = Solution().subsets([1, 2, 3])
    print(result)