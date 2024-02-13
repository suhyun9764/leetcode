from collections import deque


class MyStack:

    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()
    def push(self, x: int) -> None:
        self.que1.append(x)
    def pop(self) -> int:
        for _ in range(len(self.que1)-1):
            self.que2.append(self.que1.popleft())
            
        val = self.que1.popleft()
        self.que1, self.que2 = self.que2, self.que1
        return val
    def top(self) -> int:
        return self.que1[-1]
    def empty(self) -> bool:
        return len(self.que1) == 0