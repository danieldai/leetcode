"""
# Definition for a Node.
"""
from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque()

        queue.append(root)

        while queue:
            level_result = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level_result.append(node.val)
                if node.children:
                    queue.extend(node.children)
            result.append(level_result)
            
        return result