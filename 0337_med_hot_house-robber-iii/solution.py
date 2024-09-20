# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.robTree(root))

    def robTree(self, node: Optional[TreeNode]) -> List[int]:
        '''
         返回长度为2的数组，0：不偷，1：偷
        '''
        if not node:
            return [0, 0]
        
        left = self.robTree(node.left)
        right = self.robTree(node.right)

        # 不偷cur，那么可以偷也可以不偷左右节点，则取较大的情况
        val1 = max(left) + max(right)
        # 偷cur，那么就不能偷左右节点。
        val2 = node.val + left[0] + right[0]

        return [val1, val2]
        
        