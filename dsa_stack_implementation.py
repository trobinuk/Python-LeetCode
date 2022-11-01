from collections import deque

class Stack:
    def __init__(self):
        self.stack_lv = deque()

    def insert_value(self,val):
        self.stack_lv.append(val)

    def get_value(self):
        out_val = self.stack_lv.pop()
        return out_val

stack = Stack()
print(stack.stack_lv)

stack.insert_value(89)
stack.insert_value(26)
stack.insert_value(38)
stack.insert_value(75)

print(stack.stack_lv)

print(stack.get_value())

print(stack.stack_lv)
