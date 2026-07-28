from collections import deque

class MinStack:
    # core idea: for each stack, keep track of min value while adding new values
    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.appendleft((val, val))
        else:
            currMin = min(val, self.stack[0][1])
            self.stack.appendleft((val, currMin)) # updating current min

    def pop(self) -> None:
        self.stack.popleft()

    def top(self) -> int:
        return self.stack[0][0]

    def getMin(self) -> int:
        return self.stack[0][1]
