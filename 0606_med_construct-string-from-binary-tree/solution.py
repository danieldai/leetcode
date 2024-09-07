# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        
        if root.left is None and root.right is None:
            return str(root.val)
        
        if root.left is None and root.right is not None:
            return "%s()(%s)" % (root.val, self.tree2str(root.right))
        
        if root.left is not None and root.right is None:
            return "%s(%s)" % (root.val, self.tree2str(root.left))

        if root.left is not None and root.right is not None:
            return "%s(%s)(%s)" % (root.val, self.tree2str(root.left), self.tree2str(root.right))
