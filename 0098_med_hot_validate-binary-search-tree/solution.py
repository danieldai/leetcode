# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = self.inorder(root)

        for i in range(len(arr) - 1):
            if arr[i] >= arr[i+1]:
                return False
        
        return True

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)