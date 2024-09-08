# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre = None
        p = head

        while p is not None:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        
        return pre

        