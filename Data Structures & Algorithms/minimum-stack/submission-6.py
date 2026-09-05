class MinStack:
    # The idea is 

    def __init__(self):
        # The idea is that we have one real stack and one that
        # only contains the minimum at the current top.
        # If we pop we can then pop off of the minimum stack as well which then means
        # that
        self.stack = []
        self.curr_min = []
        

    def push(self, val: int) -> None:
        # print(f"Append {val} ({self.stack})")
        self.stack.append(val)
        if not self.curr_min:
            self.curr_min.append(val)
        else:
            new_min = min(self.curr_min[-1], val)
            self.curr_min.append(new_min)
        

    def pop(self) -> None:
        if self.stack and self.curr_min:
            self.stack.pop()
            self.curr_min.pop()
            # print(f"Popped ({self.stack})")
        

    def top(self) -> int:
        # print(f"Top ({self.stack[-1]})")
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.curr_min:
            return self.curr_min[-1]
        

        
