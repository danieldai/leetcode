# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        results = []

        cache = [root]

        while True:
            results.append(self._get_avg(cache))
            c = [n.left for n in cache if n.left is not None] + [n.right for n in cache if n.right is not None]
            cache = c
            if len(cache) == 0:
                return results
    
    def _get_avg(self, cache):
        n = len(cache)
        total = sum([n.val for n in cache])
        return total*1.0/n