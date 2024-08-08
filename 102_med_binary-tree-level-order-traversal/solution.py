# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []

        nodes = [root]
        new_nodes = []
        new_values = []

        while True:
            for node in nodes:
                new_values.append(node.val)
                if node.left is not None:
                    new_nodes.append(node.left)
                if node.right is not None:
                    new_nodes.append(node.right)
            res.append(new_values)
            nodes = new_nodes
            new_nodes = []
            new_values = []
            if len(nodes) == 0:
                return res