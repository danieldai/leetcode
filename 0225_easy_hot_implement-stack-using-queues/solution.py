from collections import deque


class MyStack:

    def __init__(self):
        self.main_queue = deque()
        self.temp_queue = deque()
        
    def push(self, x: int) -> None:
        self.main_queue.append(x)

    def pop(self) -> int:
        if len(self.main_queue) == 0:
            return None
        
        for _ in range(len(self.main_queue) - 1):
            self.temp_queue.append(self.main_queue.popleft())
        
        result = self.main_queue.popleft()

        self.main_queue, self.temp_queue = self.temp_queue, self.main_queue
        
        return result

    def top(self) -> int:
        if len(self.main_queue) == 0:
            return None
        
        for _ in range(len(self.main_queue) - 1):
            self.temp_queue.append(self.main_queue.popleft())
        
        result = self.main_queue[0]
        self.temp_queue.append(self.main_queue.popleft())

        self.main_queue, self.temp_queue = self.temp_queue, self.main_queue

        return result
        
    def empty(self) -> bool:
        return len(self.main_queue) == 0 and len(self.temp_queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()