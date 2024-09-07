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
        

class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        p1 = headA
        p2 = headB

        # when a pointer meet list end, go back to head of another head
        while p1 != p2:
            p1 = p1.next if p1 is not None else headB
            p2 = p2.next if p2 is not None else headA
        
        return p1
    

# 另一种方法，先计算出两个链表的长度，计算出长度差，在更长的链表上先走差值步数，然后两个指针一起同速移动