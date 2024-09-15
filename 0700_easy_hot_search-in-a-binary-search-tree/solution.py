# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        ptr = root

        while ptr:
            if val == ptr.val:
                break
            if val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right
        
        return ptr