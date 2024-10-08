# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return None
        
        slow = fast = head

        has_cycle = False
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                has_cycle = True
                break
        
        if has_cycle:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

        return None
        