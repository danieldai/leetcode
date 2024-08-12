# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import sys
from typing import Optional


class Solution:
    def __init__(self):
        self.ans = sys.maxsize
        
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        self.find(root, root)
        
        if self.ans == sys.maxsize:
            return -1
        else:
            return self.ans
        
    def find(self, node, root):

        if not node:
            return
        
        if node.val != root.val:
            self.ans = min(self.ans, node.val)
            return
        else:
            self.find(node.left, root)
            self.find(node.right, root)