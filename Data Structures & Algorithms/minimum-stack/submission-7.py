class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        min_elem = val
        if self.stack and self.stack[-1][1] < val:
            min_elem = self.stack[-1][1]
        self.stack.append([val, min_elem])
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
