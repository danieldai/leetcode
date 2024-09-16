# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = deque()

        addon = 0
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.right
            
            cur = stack.pop()
            cur.val += addon
            addon = cur.val
            cur = cur.left

        return root


    def convertBST2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        nodes = self.inorder(root)

        for i in range(len(nodes) - 1, 0, -1):
            nodes[i-1].val += nodes[i].val
        
        return root

    def inorder(self, root: Optional[TreeNode]) -> List[TreeNode]:
        if not root:
            return []
        
        return self.inorder(root.left) + [root] + self.inorder(root.right)
        
        