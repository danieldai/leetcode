# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)

        if not root:
            return new_node 

        ptr = root

        while True:
            if val < ptr.val:
                if ptr.left is None:
                    ptr.left = new_node
                    break
                else:
                    ptr = ptr.left
            else:
                if ptr.right is None:
                    ptr.right = new_node
                    break
                else:
                    ptr = ptr.right
        
        return root


class Solution2:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
