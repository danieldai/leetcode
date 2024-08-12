# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(val = nums[0])
        
        m = nums[0]
        p = 0

        for i, n in enumerate(nums):
            if n > m:
                m = n
                p = i
        
        root = TreeNode(val = m)
        root.left = self.constructMaximumBinaryTree(nums[:p])
        root.right = self.constructMaximumBinaryTree(nums[p+1:])

        return root