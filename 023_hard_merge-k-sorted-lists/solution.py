# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        if len(lists) == 2:
            return self.merge2Lists(lists)
        
        return self.merge2Lists([self.mergeKLists(lists[:len(lists)//2]), self.mergeKLists(lists[len(lists)//2:])])
        
    def merge2Lists(self, lists):
        
        head = None
        
        a = lists[0]
        b = lists[1]
        if not a:
            return b
        if not b:
            return a
        
        if a.val < b.val:
            head = a
            a = a.next
        else:
            head = b
            b = b.next
        p = head
        while a and b:
            if a.val < b.val:
                p.next = a
                a = a.next
            else:
                p.next = b
                b = b.next
            p = p.next
            
        if a:
            p.next = a
        elif b:
            p.next = b
            
        return head        