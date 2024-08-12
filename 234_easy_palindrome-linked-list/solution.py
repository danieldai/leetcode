# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        slow = fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        if fast is not None:
            slow = slow.next

        slow = self._reverseList(slow)

        fast = head;

        while slow is not None:
            if slow.val != fast.val:
                return False
            fast = fast.next
            slow = slow.next

        return True

    
    def _reverseList(self, head):
        prev = None

        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev

        