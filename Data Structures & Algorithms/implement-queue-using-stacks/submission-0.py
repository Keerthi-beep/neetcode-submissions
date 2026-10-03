class MyQueue:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.size>0:
            temp = []
            while self.stack:
                temp.append(self.stack.pop())
            top = temp.pop()
            while temp:
                self.stack.append(temp.pop())        
            self.size -= 1
            return top
        else:
            return None

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return self.size == 0        
