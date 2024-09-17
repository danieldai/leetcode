from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        if k == n:
            result.append([i for i in range(1, n+1)])
            return result
        
        if k == 1:
            for i in range(1, n+1):
                result.append([i])
            return result
        
        return self.combine(n - 1, k) + [ r + [n] for r in self.combine(n - 1, k - 1)]


# 回溯算法
class Solution2:

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(startIndex, n + 1):  # 需要优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点



# 回溯算法
class Solution2:

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(startIndex, n - (k - len(path)) + 2):  # 需要优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点