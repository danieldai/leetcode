# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def __init__(self):
        self.total = 0;
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = root.left

        if left is not None and left.left is None and left.right is None:
            print(left.val)
            self.total += left.val
        
        self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        return self.total