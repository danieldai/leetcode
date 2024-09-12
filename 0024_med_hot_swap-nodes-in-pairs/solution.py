# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        p1 = head
        p2 = p1.next
        head = head.next

        p0 = None
        while p1 is not None and p2 is not None:
            temp = p2.next
            p2.next = p1
            p1.next = temp
            
            if p0 is not None:
                p0.next = p2
            p0 = p1

            p1 = p1.next
            p2 = p1.next if p1 else None
            
        
        return head
    

# 使用虚拟表头，代码逻辑处理更一致
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy_head = ListNode(0, head)

        p0 = dummy_head
        p1 = head
        p2 = p1.next

        while p1 is not None and p2 is not None:
            temp = p2.next
            p2.next = p1
            p1.next = temp
            
            p0.next = p2
            p0 = p1

            p1 = p1.next
            p2 = p1.next if p1 else None
            
        
        return dummy_head.next
    

# 使用递归的方式
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        p1 = head
        p2 = p1.next

        temp = p2.next
        p2.next = p1
        p1.next = self.swapPairs(temp)

        return p2