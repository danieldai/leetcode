# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        r = p = head

        p = p.next
        r.next = None

        while p is not None:
            t = p.next
            p.next = r
            r = p
            p = t
        
        return r

        