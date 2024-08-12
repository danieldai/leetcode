# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self._get_tree_height(root) - 1 
    
        m = height + 1
        n = 2**(height+1) -1

        res = [[""]*n for _ in range(m)]

        self._fill_tree(res, root, 0 , (n-1)//2, height)

        return res

    def _fill_tree(self, res, node, r, c, height):
        if node is None:
            return
        
        res[r][c] = str(node.val)

        self._fill_tree(res, node.left, r+1, c-2**(height-r-1), height)
        self._fill_tree(res, node.right, r+1, c+2**(height-r-1), height)


    
    def _get_tree_height(self, root):
        if root is None:
            return 0
        
        return 1 + max(self._get_tree_height(root.left), self._get_tree_height(root.right))