# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:

    # 前序遍历， 中左右
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = deque()

        while root or stack:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            root = root.right

        return result


    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        