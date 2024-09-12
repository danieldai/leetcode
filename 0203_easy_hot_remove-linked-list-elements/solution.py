# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:        
        while head is not None and head.val == val:
            head = head.next

        if head is None:
            return None

        p = head

        while p is not None:
            while p.next is not None and p.next.val == val:
                p.next = p.next.next
            p = p.next
        
        return head
