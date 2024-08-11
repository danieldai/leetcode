# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        met_nodes = set()
        p = headA
        while p is not None:
            met_nodes.add(p)
            p = p.next
        
        p = headB
        while p is not None:
            if p in met_nodes:
                return p
            p = p.next
            
        return None
        