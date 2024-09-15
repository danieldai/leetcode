# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        result = []

        for suffix in self.binaryTreePaths(root.left):
            result.append(f"{root.val}->{suffix}")

        for suffix in self.binaryTreePaths(root.right):
            result.append(f"{root.val}->{suffix}")
        
        return result if result else [str(root.val)]