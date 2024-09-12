# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        dummy_head = ListNode(0, head)

        slow = dummy_head
        fast = dummy_head

        for _ in range(n):
            fast = fast.next
        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy_head.next

