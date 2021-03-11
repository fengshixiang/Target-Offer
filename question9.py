class CQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def appendTail(self, value: int) -> None:
        self.stack_1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack_2) == 0:
            while len(self.stack_1):
                self.stack_2.append(self.stack_1.pop())
        if len(self.stack_2) == 0:
            return -1
        else: 
            return self.stack_2.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()