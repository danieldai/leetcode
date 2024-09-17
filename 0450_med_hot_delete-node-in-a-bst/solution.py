# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val != key:
            root.left = self.deleteNode(root.left, key)
            root.right = self.deleteNode(root.right, key)
            return root

        if root.val == key:
            left = root.left
            right = root.right
            if left is None and right is None:
                return None
            elif left is None and right is not None:
                return right
            elif left is not None and right is None:
                return left
            else: # root.left is not None and root.right is not None
                ptr = right
                while ptr.left:
                    ptr = ptr.left
                ptr.left = left
                return right
        

class Solution2:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        parent = None
        cur = root

        while cur:
            if cur.val == key:
                break
            parent = cur
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if parent is None:
            return self.deleteOneNode(cur)
        
        if parent.left and parent.left.val == key:
            parent.left = self.deleteOneNode(cur)
        if parent.right and parent.right.val == key:
            parent.right = self.deleteOneNode(cur)

        return root

    def deleteOneNode(self, node):
        left = node.left
        right = node.right
        if not left and not right:
            return None
        elif left and not right:
            return left
        elif not left and right:
            return right
        else: # left and right
            ptr = right
            while ptr.left:
                ptr = ptr.left
            ptr.left = left
            return right


