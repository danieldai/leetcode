# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        nodes = set()

        p = head
        while p is not None:
            if p in nodes:
                return True
            nodes.add(p)
            p = p.next
        
        return False