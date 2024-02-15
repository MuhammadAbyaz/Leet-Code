from collections import deque


# using deque
class MyStack:

    def __init__(self):
        self.my_queue = deque()

    def push(self, x: int) -> None:
        self.my_queue.appendleft(x)

    def pop(self) -> int:
        return self.my_queue.popleft()

    def top(self) -> int:
        return self.my_queue[0]

    def empty(self) -> bool:
        return len(self.my_queue) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.top())
print(obj.empty())
