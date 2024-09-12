/**
 * Definition for singly-linked list.
 */

 class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
 
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null)  {
            return head;
        }

        ListNode p0 = null;
        ListNode p1 = head;
        ListNode p2 = p1.next;
        head = p2;

        while (p1 != null && p2 != null) {
            ListNode temp = p2.next;
            p2.next = p1;
            p1.next = temp;

            if(p0 != null) {
                p0.next = p2;
            }
            p0 = p1;

            p1 = p1.next;
            p2 = p1 != null ? p1.next : null;
        }

        return head;
    }
}