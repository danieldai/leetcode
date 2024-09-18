from typing import List


class Solution:

    def __init__(self) -> None:
        self.result = []
        self.path = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.backtracking(s, 0)
        return self.result

    def backtracking(self, s: str, start_index: int) -> None:
        if len(self.path) == 4:
            if start_index == len(s):
                self.result.append('.'.join(self.path))
            return 
        
        for i in range(start_index, len(s)):
            a = s[start_index:i + 1]
            if not self.is_ip_integer(a):
                continue
            self.path.append(a[:])
            self.backtracking(s, i + 1)
            self.path.pop()

    def is_ip_integer(self, s: str) -> bool:
        if len(s) > 3:
            return False
        
        if len(s) != 1 and s[0] == '0':
            return False
    
        if int(s) > 255:
            return False
        
        return True