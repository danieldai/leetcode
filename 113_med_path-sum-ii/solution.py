# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def __init__(self):
        self.a = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        left = root.left
        right = root.right
        val = root.val

        # reach leaf node
        if left is None and right is None:
            if val == targetSum:
                return [[root.val]]
            else:
                return []
        
        res = []

        if left is not None:
            res.extend(self.pathSum(left, targetSum-val))

        if right is not None:
            res.extend(self.pathSum(right, targetSum-val))

        return [[val] + r for r in res]

        
