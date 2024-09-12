class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next


# 通过使用 size 来简化边界的错误处理
class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        p = self.dummy_head.next
        for _ in range(index):
            p = p.next
        
        return p.val
        
    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        p = self.dummy_head
        while p.next is not None:
            p = p.next
        
        p.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        p = self.dummy_head
        for _ in range(index):
            p = p.next

        p.next = ListNode(val, p.next)
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        p = self.dummy_head
        for _ in range(index):
            p = p.next
        
        p.next = p.next.next
        self.size -= 1


        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# 不记录size，对边界处理比较繁琐，容易出错
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        p = self.head
        for _ in range(index + 1):
            if p.next is None:
                return -1
            p = p.next
        
        return p.val if p is not None else -1
        
    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.head.next)
        self.head.next = node
        
        
    def addAtTail(self, val: int) -> None:
        p = self.head
        while p.next is not None:
            p = p.next
        
        p.next = ListNode(val)

        

    def addAtIndex(self, index: int, val: int) -> None:
        p = self.head
        for _ in range(index):
            if p is not None:
                p = p.next
            else:
                return # no insert
        
        if p is not None:
            node = ListNode(val, p.next)
            p.next = node
        

    def deleteAtIndex(self, index: int) -> None:
        p = self.head
        for _ in range(index):
            if p is not None:
                p = p.next
            else:
                break
        
        if p is not None and p.next is not None:
            p.next = p.next.next
        
    
    def printList(self):
        l = []
        p = self.head.next
        while p is not None:
            l.append(p.val)
            p = p.next
        print(l)

        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)