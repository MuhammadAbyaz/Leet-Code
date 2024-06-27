class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0) if self.stack else -1

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack


obj = MyQueue()
obj.push(12)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
