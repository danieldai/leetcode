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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = self.inorder(root)
        
        min_diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])
        
        return min_diff

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    

# 2. 直接在中序遍历是进行计算，需要记录当前最小值和前一个节点
class Solution2:

    def __init__(self) -> None:
        self.prev = None
        self.min_diff = float('inf')

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        
        return self.min_diff

    def inorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.inorder(root.left)
        if self.prev:
            self.min_diff = min(self.min_diff, root.val - self.prev.val)
        self.prev = root
        self.inorder(root.right)


# 3. 使用中序遍历的迭代法
class Solution3:

    def __init__(self) -> None:
        self.prev = None
        self.min_diff = float('inf')

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        
        return self.min_diff

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
                self.min_diff = min(self.min_diff, cur.val - self.prev.val)
            self.prev = cur

            cur = cur.right


# 3. 使用中序遍历的迭代法2
class Solution4:

    def __init__(self) -> None:
        self.prev = None
        self.min_diff = float('inf')

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        
        return self.min_diff

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
                    self.min_diff = min(self.min_diff, cur.val - self.prev.val)
                self.prev = cur

                cur = cur.right