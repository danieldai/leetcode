# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    
    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = deque()

        prev_access = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()

            if root.right is None or root.right == prev_access:
                result.append(root.val)
                prev_access = root
                root = None
            else:
                stack.append(root)
                root = root.right
        
        return result