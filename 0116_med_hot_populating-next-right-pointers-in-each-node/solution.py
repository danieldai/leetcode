"""
# Definition for a Node.
"""

from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        queue = deque()
        
        queue.append(root)

        while queue:
            size = len(queue)
            pre_node = None

            for _ in range(size):
                cur_node = queue.popleft()
                if pre_node:
                    pre_node.next = cur_node
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                pre_node = cur_node
            
        return root
