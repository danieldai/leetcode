/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int n1 = (l1 != null) ? l1.val : 0;
        int n2 = (l2 != null) ? l2.val : 0;
        ListNode head = new ListNode((n1 + n2) % 10);
        int carry = (n1 + n2) / 10;
        
        l1 = (l1 != null) ? l1.next : null;
        l2 = (l2 != null) ? l2.next : null;
        
        ListNode p = head;
        while (l1 != null || l2 != null || carry != 0) {
            n1 = (l1 != null) ? l1.val : 0;
            n2 = (l2 != null) ? l2.val : 0;
            int val = n1 + n2 + carry;
            if (val > 9) {
                carry = val / 10;
                val %= 10;
            } else {
                carry = 0;
            }
            p.next = new ListNode(val);
            p = p.next;
            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }
        
        return head; 
    }
}