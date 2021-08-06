class Node():
        def __init__(self, val, minn, next):
            self.val = val
            self.minn = minn
            self.next = next


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = Node()


    def push(self, x: int) -> None:
        if self.head == None:
            self.head = Node(x, x, None)
        else:
            self.head = Node(x. min(self.head.minn, x), self.head)


    def pop(self) -> None:
        self.head = self.head.next


    def top(self) -> int:
        return self.head.val


    def min(self) -> int:
        return self.head.minn



obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.min()

print(param_3)
print(param_4)
