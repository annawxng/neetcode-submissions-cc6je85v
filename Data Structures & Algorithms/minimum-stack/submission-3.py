class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # need to check the empty case
        if not self.stack:
            self.stack.append(val)
            self.min_stack.append(val)
            return
        self.stack.append(val)
        curr_min = self.min_stack[-1]
        self.min_stack.append(min(val, curr_min))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return
        
