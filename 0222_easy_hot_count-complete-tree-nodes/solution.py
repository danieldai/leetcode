# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

# recursive, pass
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
    

class Solution2:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)

        count = 0

        while queue:
            size = len(queue)
            count += size

            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return count
            

class Solution3:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.countLeftDepth(root)
        right_depth = self.countRightDepth(root)

        if left_depth == right_depth:
            return 2**left_depth - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def countLeftDepth(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.left

        return depth

    def countRightDepth(self, node):
        depth = 0
        while node:
            depth += 1
            node = node.right

        return depth
