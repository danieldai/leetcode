# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next == None:
            return head

        p = head
        q = p.next

        while q is not None:
            while q is not None and q.val == p.val:
                q = q.next
            p.next = q
            p = p.next

        return head
    


class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next == None:
            return head

        p = head

        while p.next is not None:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next

        return head