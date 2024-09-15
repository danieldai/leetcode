# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == len(postorder) == 0:
            return None

        if len(inorder) == len(postorder) == 1:
            return TreeNode(inorder[0])
        
        node = TreeNode(postorder[-1])

        root_index = inorder.index(node.val)

        node.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        node.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])

        return node