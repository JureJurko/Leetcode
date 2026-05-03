class MinStack:

    def __init__(self):
        self.sums = []
        self.stack = []


    def push(self, val: int) -> None:
        if not self.sums:
            self.sums.append(val)
        elif self.sums[-1] >= val:
            self.sums.append(val)
        else:
            self.sums.append(self.sums[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.sums.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.sums[-1]

        
