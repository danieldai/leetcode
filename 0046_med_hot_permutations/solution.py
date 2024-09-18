from typing import List


class Solution:

    def __init__(self) -> None:
        self.result = []
        self.path = []
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, [False] * len(nums))
        return self.result

    def backtracking(self, nums: List[int], used: List[bool]) -> None:
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, used)
            self.path.pop()
            used[i] = False
            


if __name__ == "__main__":
    result = Solution().permute([1,2,3])
    print(result)

        