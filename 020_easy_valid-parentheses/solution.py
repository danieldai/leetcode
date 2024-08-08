from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        openings = {'(': 1, '[': 2, '{': 3}
        closings = {')': 1, ']': 2, '}': 3}
        
        stack = deque()
        
        for c in s:
            try:
                if c in openings:
                    stack.append(c)
                elif openings[stack.pop()] != closings[c]:
                    return False
            except IndexError:
                return False
        
        return not stack