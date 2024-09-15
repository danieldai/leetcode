# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = self.inorder(root)
        
        min_diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])
        
        return min_diff

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)