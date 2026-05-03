class MinStack:

    def __init__(self):
        self.sums = []
        self.stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.sums[-1] if self.sums else val)
        self.sums.append(val)

    def pop(self) -> None:
        self.sums.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.sums[-1]

        
