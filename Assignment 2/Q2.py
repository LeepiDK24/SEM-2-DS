class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self,x:int) -> None:
        self.stack1.append(x)
    
    def pop(self) -> int:
        self.move_elements_if_needed()
        return self.stack2.pop()
    
    def peek(self) -> int:
        self.move_elements_if_needed()
        return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def move_elements_if_needed(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
