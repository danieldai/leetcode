# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. 把二叉搜索树用中序遍历转为数组，这个数字是有序的，然后在数组上计算
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = self.inorder(root)

        for i in range(len(arr) - 1):
            if arr[i] >= arr[i+1]:
                return False
        
        return True

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    

# 2. 直接在中序遍历是进行计算，需要记录前一个节点
class Solution2:

    def __init__(self) -> None:
        self.prev = None
        self.isValid = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root)
        return self.isValid

    def inorder(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if self.isValid:
            self.inorder(root.left)

        if self.prev and self.isValid:
            self.isValid = root.val > self.prev.val
        self.prev = root

        if self.isValid:
            self.inorder(root.right)


# 2. 使用中序遍历的迭代法
class Solution3:

    def __init__(self) -> None:
        self.prev = None
        self.isValid = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root)
        return self.isValid

    def inorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        stack = deque()
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()

            if self.prev:
                if not cur.val > self.prev.val:
                    self.isValid = False
                    return
            self.prev = cur

            cur = cur.right


# 2. 使用中序遍历的迭代法2
class Solution4:

    def __init__(self) -> None:
        self.prev = None
        self.isValid = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root)
        return self.isValid

    def inorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        stack = deque()
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            
            else:
                cur = stack.pop()

                if self.prev:
                    if not cur.val > self.prev.val:
                        self.isValid = False
                        return
                self.prev = cur

                cur = cur.right