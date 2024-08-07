# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1.val if l1 else 0
        n2 = l2.val if l2 else 0
        head = ListNode((n1 + n2) % 10)
        carry = (n1 + n2) // 10
        
        l1 = l1.next
        l2 = l2.next
        
        p = head
        while(l1 or l2 or carry):
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            val = (n1 + n2 + carry)
            if val > 9:
                carry = val // 10
                val %= 10
            else:
                carry = 0
            p.next = ListNode(val)
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return head
        