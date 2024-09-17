# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        middle = len(nums) // 2

        root = TreeNode(nums[middle])
        
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle+1:])

        return root
    

# 使用左闭右闭区间[a, b]
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        node_que = deque()
        left_que = deque()
        right_que = deque()

        root = TreeNode(0)
        node_que.append(root)
        left_que.append(0)
        right_que.append(len(nums) - 1)

        while node_que:
            cur_node = node_que.popleft()
            left = left_que.popleft()
            right = right_que.popleft()
            middle = left + (right - left) // 2

            cur_node.val = nums[middle]

            if left <= middle - 1:
                cur_node.left = TreeNode(0)
                node_que.append(cur_node.left)
                left_que.append(left)
                right_que.append(middle - 1)
            
            if right >= middle + 1:
                cur_node.right = TreeNode(0)
                node_que.append(cur_node.right)
                left_que.append(middle + 1)
                right_que.append(right)

        return root