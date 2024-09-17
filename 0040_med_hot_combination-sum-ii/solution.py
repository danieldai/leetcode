from typing import List


class Solution:
    def __init__(self) -> None:
        self.result = []
        self.path = []
        self.sum = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtracking(candidates, target, 0)
        return self.result

    def backtracking(self, candidates: List[int], target: int, start_index: int):
        if target == self.sum:
            self.result.append(self.path[:])

        for i in range(start_index, len(candidates)):
            if i > start_index and candidates[i] ==  candidates[i-1]:
                continue
            if self.sum + candidates[i] > target:
                break
            self.path.append(candidates[i])
            self.sum += candidates[i]
            self.backtracking(candidates, target, i + 1)
            self.path.pop()
            self.sum -= candidates[i]