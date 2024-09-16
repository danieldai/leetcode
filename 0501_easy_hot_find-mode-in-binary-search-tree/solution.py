# Definition for a binary tree node.
from typing import List, Optional
from collections import Counter, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        values = self.inorder(root)

        counter = Counter(values)

        maxFre = max(counter.values())

        result = []
        for k, v in counter.items():
            if v == maxFre:
                result.append(k)

        return result

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    

# 利用搜索二叉树的特性，中序遍历该树，这样就可以对每个数字进行计数
class Solution2:

    def __init__(self) -> None:
        self.max_count = 0
        self.count = 0
        self.prev = None
        self.result = []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.searchBST(root)
        return self.result

    def searchBST(self, root: Optional[TreeNode]) -> None:
        if not root:
            return 
        
        self.searchBST(root.left)

        if not self.prev:
            self.count = 1
        elif self.prev.val == root.val:
            self.count += 1
        else:
            self.count = 1
        
        if self.count == self.max_count:
            self.result.append(root.val)

        if self.count > self.max_count:
            self.result = []
            self.max_count = self.count
            self.result.append(root.val)
        
        self.prev = root

        self.searchBST(root.right)


# 迭代法遍历
class Solution3:

    def __init__(self) -> None:
        self.max_count = 0
        self.count = 0
        self.prev = None
        self.result = []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.searchBST(root)
        return self.result

    def searchBST(self, root: Optional[TreeNode]) -> None:
        if not root:
            return 
        
        cur = root
        stack = deque()

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if not self.prev:
                self.count = 1
            elif self.prev.val == cur.val:
                self.count += 1
            else:
                self.count = 1
            
            if self.count == self.max_count:
                self.result.append(cur.val)

            if self.count > self.max_count:
                self.result = []
                self.max_count = self.count
                self.result.append(cur.val)
            
            self.prev = cur

            cur = cur.right

