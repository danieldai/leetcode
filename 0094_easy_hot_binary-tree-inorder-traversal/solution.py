# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        

# 中序遍历，左中右的顺序遍历
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = deque()

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result

