class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        next_min = val
        if self.stack:
            next_min = min(next_min, self.stack[-1][1])
        self.stack.append([val, next_min])

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
