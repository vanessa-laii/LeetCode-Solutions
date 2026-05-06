class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack:
            currMin = self.stack[-1][1]
            minElement = min(val, currMin)
        else:
            minElement = val
        self.stack.append((val, minElement))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            topElement = self.stack[-1][0]
        return topElement

    def getMin(self) -> int:
        if self.stack:
            minElement = self.stack[-1][1]
        return minElement
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()