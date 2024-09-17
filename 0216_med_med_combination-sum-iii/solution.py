from typing import List


class Solution:

    def __init__(self) -> None:
        self.result = []
        self.path = []
        self.sum = 0

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.back_tracking(k, n, 1)
        return self.result

    def back_tracking(self, k: int, n: int, start_index: int) -> None:
        if(len(self.path) == k):
            if self.sum == n:
                self.result.append(self.path[:])
            return
        
        for i in range(start_index, 9 - (k - len(self.path)) + 2):
            self.path.append(i)
            self.sum += i
            self.back_tracking(k, n, i + 1)
            self.path.pop()
            self.sum -= i
