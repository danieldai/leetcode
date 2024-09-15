# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder) ==  len(inorder) == 0:
            return None
    
        node = TreeNode(preorder[0])

        if len(preorder) == len(inorder) == 1:
            return node
        
        count = inorder.index(node.val)

        node.left = self.buildTree(preorder[1:count+1], inorder[:count])
        node.right = self.buildTree(preorder[count+1:], inorder[count+1:])

        return node

        
        