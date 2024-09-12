class ListNode {
    int val;
    ListNode next;

    public ListNode() {
        this.val = 0;
        this.next = null;
    }

    public ListNode(int val) {
        this.val = val;
        this.next = null;
    }

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
class MyLinkedList {

    ListNode dummyHead;
    int size;

    public MyLinkedList() {
        this.dummyHead = new ListNode();
        this.size = 0;
    }
    
    public int get(int index) {
        if (index < 0 || index >= size) {
            return -1;
        }

        ListNode p = this.dummyHead.next;
        for (int i = 0; i < index; i++) {
            p = p.next;
        }

        return p.val;
    }
    
    public void addAtHead(int val) {
        this.dummyHead.next = new ListNode(val, this.dummyHead.next);
        this.size++;
    }
    
    public void addAtTail(int val) {
        ListNode p = this.dummyHead;
        while (p.next != null) {
            p = p.next;
        }
        p.next = new ListNode(val);
        this.size++;
    }
    
    public void addAtIndex(int index, int val) {
        if(index < 0 || index > this.size) {
            return;
        }

        ListNode p = this.dummyHead;
        for(int i = 0; i < index; i++) {
            p = p.next;
        }
        p.next = new ListNode(val, p.next);
        this.size++;

    }
    
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= this.size) {
            return;
        }
        ListNode p = this.dummyHead;
        for (int i = 0; i < index; i++) {
            p = p.next;
        }
        p.next = p.next.next;
        this.size--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */