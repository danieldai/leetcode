# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return self._isBalanced(root)[0]
        
    def _isBalanced(self, root):
        
        if root is None:
            return True, 0
        
        left_is_balanced, left_height = self._isBalanced(root.left)
        right_is_balanced, right_height = self._isBalanced(root.right)
        
        
        return left_is_balanced and right_is_balanced and abs(left_height - right_height) <= 1, max(left_height, right_height) + 1
    