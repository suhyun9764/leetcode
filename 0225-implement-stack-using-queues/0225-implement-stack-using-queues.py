from collections import deque


class MyStack:

    def __init__(self):
        self.deq_for_push = deque()
        self.deq_for_pop = deque()

    def push(self, x: int) -> None:
        self.deq_for_push.append(x)

    def pop(self) -> int:
        while len(self.deq_for_push)>1:
            self.deq_for_pop.append(self.deq_for_push.popleft())

        pop_value=self.deq_for_push.pop()
        while len(self.deq_for_pop)>0:
            self.deq_for_push.append(self.deq_for_pop.popleft())
            
        return pop_value
    def top(self) -> int:
        while len(self.deq_for_push) > 1:
            self.deq_for_pop.append(self.deq_for_push.popleft())

        pop_value = self.deq_for_push.pop()
        while len(self.deq_for_pop) > 0:
            self.deq_for_push.append(self.deq_for_pop.popleft())
            
        self.deq_for_push.append(pop_value)

        return pop_value
    def empty(self) -> bool:
        if len(self.deq_for_push) == 0:
            return True