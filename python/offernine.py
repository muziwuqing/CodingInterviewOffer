class CQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def appendTail(self, value: int) -> None:
        self.inStack.append(value)

    def deleteHead(self) -> int:
        while len(self.outStack) != 0:
            return self.outStack.pop(-1)
        while len(self.inStack) != 0:
            self.outStack.append(self.inStack.pop(-1))
        if len(self.outStack) == 0:
            return -1;
        return self.outStack.pop(-1)


queued = CQueue()
queued.appendTail(2)
queued.appendTail(3)
print(queued.deleteHead())



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()