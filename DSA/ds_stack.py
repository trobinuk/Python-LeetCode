from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def insert_values(self,data):
        self.container.append(data)

    def last_out_values(self):
        return self.container.pop()

stac_ex = Stack()

stac_ex.insert_values('first in')
stac_ex.insert_values('second in')
stac_ex.insert_values('third in')
stac_ex.insert_values('fourth in')

print(stac_ex.container)

print(stac_ex.last_out_values())

print(stac_ex.container)
'''
class Stack:
    def __init__(self):
        self.container = []

    def insert_values(self,data):
        self.container.append(data)

    def last_out_values(self):
        return self.container.pop()


stac_ex = Stack()

stac_ex.insert_values('first in')
stac_ex.insert_values('second in')
stac_ex.insert_values('third in')
stac_ex.insert_values('fourth in')

print(stac_ex.container)

print(stac_ex.last_out_values())

print(stac_ex.container)

'''