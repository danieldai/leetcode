# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        queue = deque()

        queue.append(root.left)
        queue.append(root.right)

        while queue:
            a = queue.popleft()
            b = queue.popleft()

            if a is None and b is None:
                continue

            if a is None or b is None:
                return False

            if a.val != b.val:
                return False
            
            queue.append(a.left)
            queue.append(b.right)
            queue.append(a.right)
            queue.append(b.left)
        
        return True



    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSame(root.left, root.right)

    def isSame(self, left, right):
        if left is None and right is None:
            return True
        
        if left is None and right is not None:
            return False

        if left is not None and right is None:
            return False

        return left.val == right.val and self.isSame(left.left, right.right) and self.isSame(left.right, right.left)