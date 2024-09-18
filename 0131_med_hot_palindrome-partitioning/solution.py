from typing import List
from functools import cache

class Solution:

    def __init__(self) -> None:
        self.result = []
        self.path = []

    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s, 0)
        return self.result

    def backtracking(self, s: str, start_index: int) -> None:
        if start_index >= len(s):
            self.result.append(self.path)
            return
        
        for i in range(start_index, len(s)):
            if self.is_palindrome(s[start_index: i + 1]):
                self.path.append(s[start_index: i + 1])
            else:
                continue
            self.backtracking(s, i + 1)
            self.path.pop()
        
    def is_palindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
        
        return True


# 回文识别优化
class Solution2:

    def __init__(self) -> None:
        self.result = []
        self.path = []

    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s, 0)
        return self.result

    def backtracking(self, s: str, start_index: int) -> None:
        if start_index >= len(s):
            self.result.append(self.path)
            return
        
        for i in range(start_index, len(s)):
            if self.is_palindrome(s[start_index: i + 1]):
                self.path.append(s[start_index: i + 1])
            else:
                continue
            self.backtracking(s, i + 1)
            self.path.pop()
        
    @cache
    def is_palindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        return s[0] == s[-1] and self.is_palindrome(s[1:-1])

        

        

