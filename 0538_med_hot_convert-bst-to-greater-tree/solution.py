# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 迭代法，反中序遍历，采用右中左的遍历顺序
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
        

# 先把二叉搜索树按中序遍历转为数组，然后在数组上处理
class Solution2:

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
        

# 直接采用反中序的遍历方法来处理，边遍历边处理
class Solution3:
    def __init__(self) -> None:
        self.addon = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        self.inorder(root)

        return root

    def inorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.inorder(root.right)

        root.val += self.addon
        self.addon = root.val

        self.inorder(root.left)
        