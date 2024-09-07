from collections import deque


class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        print(f"stack1 {self.stack1} stack2 {self.stack2}")
        
        self._exchange_stack(self.stack1, self.stack2)
        
        result = self.stack2.pop()
        
        self._exchange_stack(self.stack2, self.stack1)

        return result

    def peek(self) -> int:
        self._exchange_stack(self.stack1, self.stack2)
        
        result = self.stack2[-1]
        
        self._exchange_stack(self.stack2, self.stack1)

        return result
        

    def empty(self) -> bool:
        return len(self.stack1) == 0


    def _exchange_stack(self, from_stack, to_stack):
        while len(from_stack) > 0:
            to_stack.append(from_stack.pop())
        

class MyQueue:

    def __init__(self):
        self.in_stack = deque()
        self.out_stack = deque()

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if len(self.out_stack) == 0:
            self._in_to_out()
        
        if len(self.out_stack) > 0:
            return self.out_stack.pop()
        else:
            return None

    def peek(self) -> int:
        if len(self.out_stack) == 0:
            self._in_to_out()
        
        if len(self.out_stack) > 0:
            return self.out_stack[-1]
        else:
            return None
        
    def empty(self) -> bool:
        return len(self.in_stack) == 0 and len(self.out_stack) == 0


    def _in_to_out(self):
        while len(self.in_stack) > 0:
            self.out_stack.append(self.in_stack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()